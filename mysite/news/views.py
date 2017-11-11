# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoadForm, AddArticleForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
# Create your views here.


def index(request):
    if request.method == 'POST':
        login_form = LoadForm(request.POST)
        if login_form.is_valid():
            form_login_email = login_form.cleaned_data["email"]
            form_login = login_form.cleaned_data["password"]
            print form_login_email
            print form_login
            user = User.objects.filter(email=form_login_email, password=form_login).first()

            # auth_user = authenticate(email=user.email, password=user.password)
            if user.is_active:
                login(request, user)
            return render(request, 'index.html', {"form": LoadForm()})

    return render(request, 'index.html', {"form": LoadForm()})


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


def logout_view(request):
    logout(request)
    return redirect('/')


def add_article(request):
    add_article_form = AddArticleForm()

    return render(request, 'add_article', {"add_article_form": AddArticleForm()})
