from django.views.generic import ListView
from django.shortcuts import render
from .models import Post, Subject


def index_page(request):
    return render(request, 'index.html')


def sign_in(request):
    return render(request, 'sign_in.html')


def sign_up(request):
    return render(request, 'sign_up.html')


def sections(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'sections.html', context)


def by_section(request, subject_id):
    posts = Post.objects.filter(subject=subject_id)
    context = {'posts': posts}
    return render(request, 'by_section.html', context)



