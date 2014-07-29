from django.conf import settings


SUBSCRIBE_ACTIVATION_DAYS = getattr(settings, 'SUBSCRIBE_ACTIVATION_DAYS', 7)
SUBSCRIBE_EMAILS_SENDER = getattr(settings, 'SUBSCRIBE_EMAILS_SENDER', 'email@subscribe.com')
