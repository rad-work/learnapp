from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Post, Subject
from post.forms import SignUpForm, SignInForm
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'index.html'


def index_page(request):
    return render(request, 'index.html')


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Авторизация успешна")
                return redirect(index_page)
            else:
                messages.add_message(request, messages.ERROR, "Неправильный логин или пароль")
                form = SignInForm()
                return render(request, 'sign_in.html', {'form': form, })
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме авторизации")
            form = SignInForm()
            return render(request, 'sign_in.html', {'form': form, })
    else:
        form = SignInForm()
        return render(request, 'sign_in.html', {'form': form, })


def by_post(request, post_id):
    posts = Post.objects.filter(id=post_id)
    context = {'posts': posts}
    return render(request, 'by_post.html', context)


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            email = form.data['email']
            password = form.data['password']

            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, "Данный логин уже существует")
                form = SignUpForm()
                return render(request, 'sign_up.html', {'form': form, })
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Регистрация прошла успешно")
                return redirect(index_page)
        else:
            messages.add_message(request, messages.ERROR, "Некорректные данные в форме регистрации")
            form = SignUpForm()
            return render(request, 'sign_up.html', {'form': form, })
    else:
        form = SignUpForm()
        return render(request, 'sign_up.html', {'form': form, })


def sections(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'sections.html', context)


def by_section(request, subject_id):
    posts = Post.objects.filter(subject=subject_id)
    context = {'posts': posts}
    return render(request, 'by_section.html', context)


def log_out(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Вы успешно вышли из аккаунта")
    return redirect(index_page)
