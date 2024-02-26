# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django_recaptcha.fields import ReCaptchaField


class MyForm(forms.Form):
    captcha = ReCaptchaField()