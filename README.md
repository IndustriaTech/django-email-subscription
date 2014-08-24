# django-email-subscription

This app is **NOT** connected with django user model.

It is just email subscription system, providing users with functionally where they can register
their email and receive newsletters.

This app needs:
- [django-simple-captcha](https://github.com/mbi/django-simple-captcha)

It will be automatically installed so no worries.


## SetUp

Install the app:

    pip install git+git://github.com/MagicSolutions/django-email-subscription.git

You should have these in installed apps:

    INSTALLED_APPS = (
        ....

        'captcha',
        'email_subscription',
    )

Add the urls in your main urls.py file:

    url(r'^captcha/', include('captcha.urls')),
    url(r'^subscribe/', include('email_subscription.urls', namespace='subscriptions'))

Run migrations or syncdb depending on whether you use South.

You can add custom app configurations in settings.py

    SUBSCRIBE_ACTIVATION_DAYS  # default is 7
    SUBSCRIBE_EMAILS_SENDER  # default is 'email@subscribe.com'

And off you go.
