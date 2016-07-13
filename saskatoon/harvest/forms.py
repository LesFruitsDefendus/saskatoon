# coding: utf-8

from time import timezone

import datetime
from django import forms
from dal import autocomplete
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div
from harvest.models import *
from member.models import *
from django.core.mail import send_mail

class RequestForm(forms.ModelForm):
    picker_email = forms.EmailField(help_text=_("Enter a valid email address, please."), label=_("Email"))
    picker_first_name = forms.CharField(label=_("First name"))
    picker_family_name = forms.CharField(label=_("Family name"))
    picker_phone = forms.CharField(label=_("Phone"))
    picker_comment = forms.CharField(label=_("Comment"), required=False, widget=forms.widgets.Textarea())
    harvest_id = forms.CharField(widget=forms.HiddenInput())
    notes_from_pickleader = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        email = self.cleaned_data['picker_email']
        auth_user_count = AuthUser.objects.filter(email=email).count()
        if auth_user_count > 0: # check if email is already in the database
            auth_user = AuthUser.objects.get(email=email)
            harvest_obj = Harvest.objects.get(id=self.cleaned_data['harvest_id'])
            request_same_user_count = RequestForParticipation.objects.filter(picker = auth_user.person, harvest = harvest_obj).count()
            if request_same_user_count > 0: # check if email has requested for the same harvest
                raise forms.ValidationError, _("You have already requested to join this pick.")

    def send_email(self, subject, message, mail_to):
        send_mail(
                subject,
                message,
                'info@lesfruitsdefendus.org',
                mail_to,
                fail_silently=False,
            )

    def save(self):
        instance = super(RequestForm, self).save(commit=False)

        harvest_id = self.cleaned_data['harvest_id']
        first_name = self.cleaned_data['picker_first_name']
        family_name = self.cleaned_data['picker_family_name']
        phone = self.cleaned_data['picker_phone']
        email = self.cleaned_data['picker_email']
        comment = self.cleaned_data['picker_comment']
        harvest_obj = Harvest.objects.get(id=harvest_id)

        # check if the email is already registered
        auth_user_count = AuthUser.objects.filter(email = email).count()

        if auth_user_count > 0: # user is already in the database
            auth_user = AuthUser.objects.get(email=email)
            instance.picker = auth_user.person
            instance.harvest = harvest_obj
        else: # user is not in the database, so create a new one and link it to Person obj
            instance.picker = Person.objects.create(first_name=first_name, family_name=family_name, phone=phone)
            auth_user = AuthUser.objects.create(email=email, person=instance.picker)


        # Building email content
        pick_leader_email = []
        pick_leader_email.append(str(harvest_obj.pick_leader.email))
        pick_leader_name  = harvest_obj.pick_leader.person.first_name
        publishable_location = harvest_obj.property.publishable_location
        mail_subject = _(u"New request from ") + "%s %s" % (first_name, family_name)
        message = u"Hi %s, \n\n\
There is a new request from %s to participate in harvest #%s at '%s'.\n\n\
Full name: %s %s\n\
Email: %s\n\
Phone: %s\n\
Comment: %s\n\n\
Please contact %s directly and then manage this request through\n\
http://saskatoon.lesfruitsdefendus.org/harvest/%s\n\n\
Yours,\n\
--\n\
Saskatoon Harvest System"  % (pick_leader_name, first_name, harvest_id, publishable_location, first_name, family_name, email, phone, picker_comment, first_name, harvest_id)

        # Sending email to pick leader
        self.send_email(mail_subject, message, pick_leader_email)

        instance.save()

        return instance

    class Meta:
        model = RequestForParticipation
        fields = [
            'number_of_people',
            'picker_first_name',
            'picker_family_name',
            'picker_email',
            'picker_phone',
            'picker_comment',
            'harvest_id',
            'notes_from_pickleader'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': _(u"Your comment here.")
                }
            ),
        }

# To be used by the pick leader to accept/deny/etc and add notes on a picker
class RFPManageForm(forms.ModelForm):
    STATUS_CHOICES = [('showed_up', _('Picker showed up')), ('didnt_showed_up', _("Picker didn't show up")), ('cancelled', _("Picker cancelled in advance"))]
    ACCEPT_CHOICES = [('yes', _('ACCEPT')), ('no', _("REFUSE")), ('pending', _("PENDING"))]
    accept = forms.ChoiceField(label=_('Please accept or refuse this request :'), choices=ACCEPT_CHOICES, widget=forms.RadioSelect(), required=False)
    status = forms.ChoiceField(label=_('About the picker partition :'), choices=STATUS_CHOICES, widget=forms.RadioSelect(), required=False)

    class Meta:
        model = RequestForParticipation
        fields = ['accept','status', 'notes_from_pickleader']

    def save(self):
        instance = super(RFPManageForm, self).save(commit=False)
        status = self.cleaned_data['status']
        accept = self.cleaned_data['accept']

        if accept == 'yes':
            instance.acceptation_date = datetime.datetime.now()
            instance.is_accepted = True
        elif accept == 'no':
            instance.acceptation_date = None
            instance.is_accepted = False
        elif accept == 'pending':
            instance.acceptation_date = None
            instance.is_accepted = None


        instance.save()
        return instance

# Used in admin interface
class RFPForm(forms.ModelForm):
    class Meta:
        model = RequestForParticipation
        fields = '__all__'

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = [
            'image'
        ]

class HarvestImageForm(forms.ModelForm):
    class Meta:
        model = HarvestImage
        fields = [
            'image'
        ]


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'is_active',
            'owner',
            'trees',
            'trees_location',
            'avg_nb_required_pickers',
            'public_access',
            'neighbor_access',
            'compost_bin',
            'street_number',
            'street',
            'complement',
            'postal_code',
            'publishable_location',
            'neighborhood',
            'city',
            'state',
            'country',
            'longitude',
            'latitude',
            'about',
        )
        widgets = {
            'owner': autocomplete.ModelSelect2(
               'actor-autocomplete'
            ),
            'trees': autocomplete.ModelSelect2Multiple(
                'tree-autocomplete'
            ),
            'about': forms.Textarea(),
            'avg_nb_required_pickers': forms.NumberInput()
        }


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        help_texts = {
            'status': 'test',
        }
        fields = (
            'status',
            'property',
            'trees',
            'owner_present',
            'owner_help',
            'owner_fruit',
            'pick_leader',
            'start_date',
            'end_date',
            'nb_required_pickers',
            'about',
        )
        widgets = {
            'trees': autocomplete.ModelSelect2Multiple(
                'tree-autocomplete'
            ),
            'pickers': autocomplete.ModelSelect2Multiple(
                'person-autocomplete'
            ),
            'pick_leader': autocomplete.ModelSelect2(
                'pickleader-autocomplete'
            ),
            'equipment_reserved': autocomplete.ModelSelect2Multiple(
                'equipment-autocomplete'
            ),
            'property': autocomplete.ModelSelect2(
                'property-autocomplete'
            ),
            'nb_required_pickers': forms.NumberInput()
        }

    publication_date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    start_date = forms.DateTimeField(
        input_formats=('%Y-%m-%d %H:%M',),
        widget=forms.DateInput(
            format='%Y-%m-%d %H:%M',
        )
    )

    end_date = forms.DateTimeField(
        input_formats=('%Y-%m-%d %H:%M',),
        widget=forms.DateInput(
            format='%Y-%m-%d %H:%M',
        )
    )

    def save(self):
        instance = super(HarvestForm, self).save(commit=False)

        status = self.cleaned_data['status']
        publication_date = self.cleaned_data['publication_date']
        trees = self.cleaned_data['trees']

        if status in ["Ready", "Date-scheduled", "Succeeded"]:
    #        if publication_date is None:
            instance.publication_date = timezone.now()

        if status in ["To-be-confirmed", "Orphan", "Adopted"]:
            if publication_date is not None:
                instance.publication_date = None

        if not instance.id:
            instance.save()
        instance.trees = trees
        instance.save()

        return instance


class HarvestYieldForm(forms.ModelForm):
    class Meta:
        model = HarvestYield
        fields = ('__all__')
        widgets = {
            'recipient': autocomplete.ModelSelect2(
                'actor-autocomplete'
            ),
            'tree': autocomplete.ModelSelect2(
                'tree-autocomplete'
            ),
        }


class EquipmentForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(EquipmentForm, self).clean()

        if not (bool(self.cleaned_data['property']) != bool(self.cleaned_data['owner'])):
            raise forms.ValidationError, _('Fill in one of the two fields: property or owner.')

        return cleaned_data

    class Meta:
        model = Equipment
        widgets = {
            'property': autocomplete.ModelSelect2(
                'property-autocomplete'
            ),
            'owner': autocomplete.ModelSelect2(
                'actor-autocomplete'
            ),
        }
        fields = ('__all__')

