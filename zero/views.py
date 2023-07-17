from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

menu=[{'title': 'About site', 'url_name': 'about'},
      {'title': 'Add page', 'url_name': 'addpage'},
      {'title': 'Contact', 'url_name': 'contact'},
      {'title': 'Login', 'url_name': 'login'}
      ]

def index(request):
    posts=Man.objects.all()
    context ={
        'posts': posts,
        'menu': menu,
        'title':'main page',
        'cat_selected':0,
    }
    return render(request, 'zero/index.html', context=context)

def about(request):
    return render(request, 'zero/about.html', {'menu': menu,'title': 'page about site'})

def addpage(request):
    return HttpResponse('<h1>add page</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def show_post(request, post_id):
    post=get_object_or_404(Man, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'zero/post.html', context=context)

def show_category(request, cat_id):
    posts = Man.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'main page',
        'cat_selected': cat_id,
    }
    return render(request, 'zero/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>this page not found</h1>')