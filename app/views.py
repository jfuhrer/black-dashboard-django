# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import PersonTest

@login_required(login_url="/login/")
def index(request):
    context = {}
    try:
        username = None
        username = request.user.username
        userId = request.user
        print('userId ', userId)
        if username is None:
            print('username is none')  # ToDo: throw better exception
        else:
            print('get advisory sessions for user', username)
        persons = PersonTest.objects.filter(first_name=username) # ToDo: maybe select with id, not username?

        context = {'persons': persons}
        context['segment'] = 'index'

        return render(request, "index.html", {'persons': persons})

    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    #html_template = loader.get_template( 'index.html' )
    #return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def advisorySessions(request):
    context = {}

    try:
        username = None
        username = request.user.username
        userId = request.user
        print(userId)
        if username is None:
            print('username is none')  # ToDo: throw better exception
        else:
            print('get advisory sessions for user', username)

        persons = PersonTest.objects.filter(first_name=username)
        context = {'persons': persons}

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        return render(request, "advisorySession.html", context)


    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
