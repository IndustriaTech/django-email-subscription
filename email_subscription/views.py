from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView
from django.http import Http404

from email_subscription.forms import EmailSubscriberForm
from email_subscription.models import EmailSubscriber, ActivationKeyExpired


class RegistrationView(FormView):
    template_name = 'email_subscription/registration_form.html'
    form_class = EmailSubscriberForm
    success_url = reverse_lazy('subscriptions:activation_mail_sent')

    def form_valid(self, form):
        form.save()
        form.instance.send_activation_email(site=Site.objects.get_current())
        return super(RegistrationView, self).form_valid(form)


class ActivationView(RedirectView):
    http_method_names = ['get']
    url = reverse_lazy('subscriptions:activation_complete')

    def get_redirect_url(self, *args, **kwargs):
        try:
            to_activate = EmailSubscriber.objects.get_nonexpired(
                activation_key__exact=kwargs['activation_key'], is_activated=False)
        except EmailSubscriber.DoesNotExist:
            raise Http404
        except ActivationKeyExpired:
            return reverse_lazy('subscriptions:activation_closed')
        else:
            to_activate.is_activated = True
            to_activate.save()
            return self.url


class DeactivationView(RedirectView):
    http_method_names = ['get']
    url = reverse_lazy('subscriptions:deactivate_complete')

    def get_redirect_url(self, *args, **kwargs):
        try:
            to_deactivate = EmailSubscriber.objects.active().get(
                activation_key__exact=kwargs['activation_key'])
        except EmailSubscriber.DoesNotExist:
            raise Http404
        else:
            to_deactivate.is_activated = False
            to_deactivate.save()
            return self.url


class ActivationClosedView(TemplateView):
    template_name = "email_subscription/activation_closed.html"


class ActivationCompleteView(TemplateView):
    template_name = "email_subscription/activation_complete.html"


class CheckMailView(TemplateView):
    template_name = "email_subscription/check_mail.html"


class DeactivationCompleteView(TemplateView):
    template_name = "email_subscription/deactivate_complete.html"
