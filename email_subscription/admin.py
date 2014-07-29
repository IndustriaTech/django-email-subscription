from django.contrib import admin
from email_subscription.models import EmailSubscriber


class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_activated')


admin.site.register(EmailSubscriber, EmailSubscriberAdmin)
