import datetime

from django.core.mail import EmailMessage
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from email_subscription import settings


class ActivationTimeExpired(Exception):
    pass


class EmailSubscriber(models.Model):
    email = models.EmailField(_('email address'))
    activation_key = models.CharField(_('activation key'), max_length=40)
    is_activated = models.BooleanField(_('subscriber activated'), default=False)
    activation_request_sent_at = models.DateTimeField(_('date joined'), default=timezone.now)

    ActivationTimeExpired = ActivationTimeExpired

    def activation_key_expired(self):
        expiration_date = self.activation_request_sent_at + datetime.timedelta(
            days=settings.SUBSCRIBE_ACTIVATION_DAYS)
        return self.is_activated or expiration_date <= timezone.now()
    activation_key_expired.boolean = True

    def deactivation_url(self):
        return 'http://{site_domain}{link}'.format(
            site_domain=Site.objects.get_current().domain,
            link=reverse('subscriptions:deactivation', args=[self.activation_key])
        )

    def activation_url(self):
        return 'http://{site_domain}{link}'.format(
            site_domain=Site.objects.get_current().domain,
            link=reverse('subscriptions:activation', args=[self.activation_key])
        )

    def send_activation_email(self, site):
        context = {
            'activation_url': self.activation_url(),
            'expiration_days': settings.SUBSCRIBE_ACTIVATION_DAYS,
            'site': site
        }

        subject = _('Email subscription for {}'.format(site))
        body = render_to_string('email_subscription/activation_email.html', context)
        from_email = settings.SUBSCRIBE_EMAILS_SENDER

        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email=from_email,
            to=[self.email],
        )
        mail.send()

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')
