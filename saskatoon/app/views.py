import datetime

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from harvest.models import Harvest, Property, RequestForParticipation
from harvest.forms import RequestForm



########## Original template views #############

def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

############ 'pages' views ####################

class Calendar(generic.TemplateView):
    template_name = 'app/calendar.html'

    def dispatch(self, request, *args, **kwargs):
        return super(Calendar, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Calendar, self).get_context_data(**kwargs)

        context['view'] = "calendar"
        context['form_request'] = RequestForm()

        return context

class JsonCalendar(generic.View):
    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start')
        end_date = request.GET.get('end')
        ed = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        sd = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        harvests = Harvest.objects.filter(end_date__lte=ed, start_date__gte=sd)
        events = []
        for harvest in harvests:
            if (harvest.start_date and
                    harvest.end_date and
                    self.request.user.is_staff) \
                    or harvest.is_publishable():
                text_color = "#ffffff"
                if harvest.status == "Date-scheduled":
                    color = "#f0ad4e"
                elif harvest.status == "Ready":
                    color = "#337ab7"
                elif harvest.status == "Succeeded":
                    color = "#26B99A"
                elif harvest.status == "Cancelled":
                    color = "#D9534F"
                else:
                    color = "#ededed"
                    text_color = "#333"
                event = dict()
                event["harvest_id"] = harvest.id
                event["allday"] = "false"
                event["description"] = harvest.about
                event["status"] = harvest.status
                event["nb_required_pickers"] = harvest.nb_required_pickers
                requests_count = RequestForParticipation.objects.filter(harvest=harvest).count()
                event["nb_requests"] = requests_count
                trees_list = []
                for t in harvest.trees.all():
                    trees_list.append(t.fruit_name)
                event["trees"] = trees_list
                event["title"] = ", ".join(trees_list)
                if harvest.property.neighborhood.name != "Other":
                    event["title"] += " @ "+harvest.property.neighborhood.name
                
                event["total_harvested"] = harvest.get_total_distribution()

                # FIXME: see
                # http://fullcalendar.io/docs/event_rendering/eventRender/
                if harvest.start_date:
                    tz_start_date = harvest.start_date - datetime.timedelta(hours=4)
                    event["start"] = tz_start_date
                    event["start_date_str"] = tz_start_date.strftime("%Y-%m-%d")
                    event["start_time"] = tz_start_date.strftime("%H:%M")
                # FIXME: ugly hack, needs proper interaction with calendar
                # http://fullcalendar.io/docs/timezone/timezone/
                if harvest.end_date:
                    tz_end_date = harvest.end_date - datetime.timedelta(hours=4)
                    event["end"] = tz_end_date
                    event["end_time"] = tz_end_date.strftime("%H:%M")
                event["url"] = reverse(
                    'harvest:participation_create',
                    kwargs={'pk': harvest.id}
                )
                event["color"] = color
                event["textColor"] = text_color
                events.append(event)
                del event

        return JsonResponse(events, safe=False)



