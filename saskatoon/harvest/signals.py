from crequest.middleware import CrequestMiddleware
from django.core.mail import send_mail


def _send_mail(subject, message, mail_to):
    subject = '[Sakatoon] ' + subject
    send_mail(
            subject,
            message,
            'info@lesfruitsdefendus.org',
            mail_to,
            fail_silently=False,
        )


def changed_by(sender, instance, **kwargs):
    current_request = CrequestMiddleware.get_request()
    if current_request:
        # If property is created by the owner not authenticated:
        if current_request.user.is_anonymous is False:
            instance.changed_by = current_request.user
    else:
        instance.changed_by = None


def comment_send_mail(sender, instance, **kwargs):
    current_request = CrequestMiddleware.get_request()

    # Send email only if comment comes from someone else
    if instance.author.email != instance.harvest.pick_leader.email:
        # Building email content
        pick_leader_email = list()
        pick_leader_email.append(instance.harvest.pick_leader.email)
        pick_leader_name = instance.harvest.pick_leader.person.first_name
        mail_subject = u"New comment from %s" % instance.author
        message = u'Hi %s, \n\n' \
                  u'On %s %s left the following comment\n' \
                  u'in the harvest "%s":\n\n' \
                  u'%s\n\n' \
                  u'You can see all comments related to this ' \
                  u'harvest at\n' \
                  u'http://saskatoon.lesfruitsdefendus.org/harvest/%s.' \
                  u'\n\n' \
                  u'Yours,\n' \
                  u'--\n' \
                  u'Saskatoon Harvest System' % \
                  (
                      pick_leader_name,
                      instance.created_date.strftime('%b %d at %H:%M'),
                      instance.author,
                      instance.harvest.property.publishable_location,
                      instance.content,
                      instance.harvest.id
                  )

        # Sending email to pick leader
        _send_mail(mail_subject, message, pick_leader_email)
