from django.conf.urls import url, patterns

from email_subscription.views import (
    ActivationClosedView,
    ActivationCompleteView,
    ActivationView,
    CheckMailView,
    DeactivationCompleteView,
    DeactivationView,
    RegistrationView,
)


urlpatterns = patterns(
    '',
    url(r'^activation/closed/$', ActivationClosedView.as_view(), name='activation_closed'),
    url(r'^activation/complete/$', ActivationCompleteView.as_view(), name='activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='activation'),
    url(r'^checkmail/$', CheckMailView.as_view(), name='activation_mail_sent'),
    url(r'^deactivate/complete/$', DeactivationCompleteView.as_view(), name='deactivate_complete'),
    url(r'^deactivate/(?P<activation_key>\w+)/$', DeactivationView.as_view(), name='deactivation'),
    url(r'^request/$', RegistrationView.as_view(), name='request'),
)
