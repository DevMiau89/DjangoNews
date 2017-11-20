# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, LoadForm, AddArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
# Create your views here.


def index(request):
    top_articles = Article.objects.all().order_by("-created_date")[:5]
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
            return render(request, 'article_detail.html', {"form": LoadForm()})

    return render(request, 'index.html', {"form": LoadForm(), "top_articles": top_articles})


def registration(request):
    # register_form = RegistrationForm()
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

    return render(request, 'registration.html', {"register_form": RegistrationForm(), "form": LoadForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def add_article(request):
    # add_article_form = AddArticleForm()
    if request.method == 'POST':
        add_article_form = AddArticleForm(request.POST, request.FILES)
        print add_article_form

        if add_article_form.is_valid():
            add_article_form.save()
            return render(request, 'add_article.html', {"add_article_form": AddArticleForm(), "form": LoadForm()})

    return render(request, 'add_article.html', {"add_article_form": AddArticleForm(), "form": LoadForm()})


def article_detail(request, id=None):
    instance = get_object_or_404(Article, id=id)
    comments = instance.comments.filter(active=True)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article_id = instance.id
            new_comment.save()

        else:
            comment_form = CommentForm()
        return render(request, 'article_detail.html', {"form": LoadForm(),
                                                       "instance": instance,
                                                       'comments': comments,
                                                       'comment_form': comment_form
                                                       })

    return render(request, 'article_detail.html', {"form": LoadForm(),
                                                   "instance": instance,
                                                   'comments': comments,
                                                   'comment_form': comment_form
                                                   })


def contact(request):
    return render(request, 'contact.html', {"form": LoadForm()})
