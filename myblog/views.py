from .models import Post
from django.shortcuts import render
from .forms import form_model

from django.db.models import Avg, Count


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
    return render(request, 'myblog/my_form.html', {'form': form})


def about(request):
    titles = Post.objects.order_by('title')

    return render(request, 'myblog/about.html',
                  {'titles': titles},

                  )


def avg(request):
    avg = Post.objects.aggregate(Avg('age'))

    return render(request, 'myblog/avg.html',
                  {'avg': avg},)


def count(request):
    count = Post.objects.count()
    return render(request, 'myblog/count.html',
                  {'count': count}, )
