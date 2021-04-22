from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'index.html'


def index_page(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def themes(request):
    return render(request, 'themes.html')


def sections(request):
    return render(request, 'sections.html')


def paragraph_1(request):
    return render(request, 'paragraph_1.html')
