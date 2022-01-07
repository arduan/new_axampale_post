from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Post
from django.shortcuts import render
from .forms import form_model






def show(request):
    titles = Post.objects.order_by('title')
    return render(request, 'myblog/example.html', {
        'titles': titles,
    })


def one_show(request, id_title: int):
    title = Post.objects.get(id=id_title)
    return render(request, 'myblog/test.html', {
        'title': title,

    })

def get_name(request):
    form = form_model(request.POST)
    return render(request, 'my_form.html', {'form': form})

def about(request):
    return render(request, 'myblog/about.html')

