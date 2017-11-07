# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def registration(request):
    register_form = RegistrationForm()
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            form_name = register_form.cleaned_data["first_name"]
            form_surname = register_form.cleaned_data["last_name"]
            form_email = register_form.cleaned_data["email"]
            form_password = register_form.cleaned_data["password"]
            feedback = User(username=form_name, first_name=form_name, last_name=form_surname, email=form_email, password=form_password)
            feedback.save()
            return render(request, 'registration.html', {"register_form": register_form})

    return render(request, 'registration.html', {"register_form": register_form})
