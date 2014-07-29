import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-email-subscription',
    url='https://github.com/MagicSolutions/django-email-subscription',
    version='0.0.1',
    description='Django app for creating subcription accoutns.',
    long_description=README,
    install_requires=[
        'django-simple-captcha>=0.4.2',
    ],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
