from .models import Post
from django.shortcuts import render
from .forms import form_model


import matplotlib.pyplot as plt
import numpy as np

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
    form = form_model(request.POST)
    return render(request, 'myblog/about.html', {'form': form})


def graph(request):
    loss = np.array([1, 0.95, 0.92, 0.89, 0.83, 0.76, 0.70, 0.63, 0.54, 0.48])
    epochs = np.array(list(range(10)))
    plt.plot(loss, epochs, label="Loss Curve 1", linestyle="dashed", marker='*', color='red')
    # Plot 1
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    # Plot 2
    plt.title("Loss - Epoch Curve")
    # Plot 3
    plt.grid("on")
    # Plot 4
    plt.legend()
    # Plot 5
    plt.show()
    return render('myblog/about.html', {'graph': graph})