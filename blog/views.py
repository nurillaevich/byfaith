from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.


def home(req):
    navb = HomePage.objects.all()

    post = Home.objects.order_by('-id')[:2]
    sermon = Sermons.objects.all()
    us = About.objects.all()
    tag = Tag.objects.all()
    test = Testimonial.objects.all()
    author = Author.objects.all()
    our = OurS.objects.all()
    context = {
        'posts': post,
        'sermons': sermon,
        'uses': us,
        'tags': tag,
        'tests': test,
        'authors': author,
        'ours': our,
        'home': navb
    }
    return render(req, 'index-2.html', context)


def sermons(req):
    sermon = Sermons.objects.all()
    us = About.objects.all()
    test = Testimonial.objects.all()
    tag = Tag.objects.all()
    our = OurS.objects.all()
    context = {
        'sermons': sermon,
        'uses': us,
        'tests': test,
        'tags': tag,
        'ours': our
    }
    return render(req, 'sermons.html', context)


def ministries(req):
    post = Ministries.objects.all()
    wha = About.objects.all()
    tag = Tag.objects.all()
    context = {
        'posts': post,
        'what': wha,
        'tags': tag,
    }
    return render(req, 'ministry.html', context)


def events(req):
    e = Events.objects.all()
    a = About.objects.all()
    t = Tag.objects.all()
    context = {
        'events': e,
        'about': a,
        'tags': t,
    }
    return render(req, 'events.html', context)


def detail_page(request, pk):
    post = get_object_or_404(Sermons, pk=pk)
    releted_sermons = Sermons.objects.all().order_by("-id")[:3]
    context = {
        'details': post,
        'sermons': releted_sermons
    }
    return render(request, 'sermon-single.html', context)
