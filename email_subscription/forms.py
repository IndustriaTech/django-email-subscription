import random
import hashlib

from django.utils import timezone
from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField

from email_subscription.models import EmailSubscriber


def generate_activation_key(email):
    if isinstance(email, str):
        email = email.encode('utf-8')
    salt = hashlib.md5(str(random.random())).hexdigest()[:10]
    return hashlib.md5(salt+email).hexdigest()


class EmailSubscriberForm(forms.ModelForm):
    email = forms.EmailField(max_length=256, label=_('Email'), required=True)
    captcha = CaptchaField(label=_('Security code'))
    activation_key = forms.CharField(widget=forms.HiddenInput(), required=False)
    activation_request_sent_at = forms.DateField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = EmailSubscriber
        fields = (
            'email',
            'activation_key',
            'activation_request_sent_at',
        )

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            self.instance = EmailSubscriber.objects.get(email__iexact=email)
            if self.instance is not None:
                return email.lower()
        except EmailSubscriber.DoesNotExist:
            return email.lower()
        raise forms.ValidationError(_('This email is already subscribed.'))

    def clean(self):
        data = self.cleaned_data
        if 'email' in data:
            self.cleaned_data['activation_key'] = generate_activation_key(data['email'])
            self.cleaned_data['activation_request_sent_at'] = timezone.now()
        return self.cleaned_data
