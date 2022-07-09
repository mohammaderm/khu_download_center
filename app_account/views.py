from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app_account.forms import ProfileForm, SignUpForm, Softrequestform, Booksendform
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from app_social.models import Bookmark
from app_software.models import Software
from app_account.models import Softrequest
from django.http import HttpResponse, HttpResponseRedirect
from app_book.models import Book
from app_book.models import Category
from app_book.models import Files
from django.contrib import messages
# from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('app_software:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def Profile(request):
    ctx = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, user=request.user)
        ctx['form'] = form
        if form.is_valid():
            form.save()
            ctx['form'] = form
    else:
        init_dict = {**request.user.profile.__dict__, **request.user.profile.user.__dict__}
        ctx['form'] = form = ProfileForm(initial=init_dict)
    return render(request, 'dashboard.html', ctx)


@login_required
def bookmarksdisplay(request):
    ctx = {}
    ctx['bookmark'] = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmark.html', ctx)


@login_required
def softrequest(request):
    ctx = {}
    if request.method == 'POST':
        form = Softrequestform(request.POST)
        if form.is_valid():
            softr = form.save()
            softr.user = request.user
            softr.softname = form.cleaned_data.get('softname')
            softr.description = form.cleaned_data.get('description')
            form.save()
            ctx['form'] = form = Softrequestform()
            ctx['disrequest'] = Softrequest.objects.filter(user=request.user).order_by('-publish_date')
            return render(request, 'request.html', ctx)
    else:
        ctx['form'] = form = Softrequestform()
        ctx['disrequest'] = Softrequest.objects.filter(user=request.user).order_by('-publish_date')
    return render(request, 'request.html', ctx)


@login_required
def booksend(request):
    ctx = {}
    if request.method == 'POST':
        form = Booksendform(request.POST, request.FILES)
        if form.is_valid():
            books = form.save()
            books.user = request.user
            books.title = form.cleaned_data.get('title')
            books.author = form.cleaned_data.get('author')
            books.description = form.cleaned_data.get('description')
            books.category = form.cleaned_data.get('category')
            books.image = form.cleaned_data.get('image')
            books.files_set.create(file=form.cleaned_data.get('file'))
            form.save()
            ctx['form'] = form = Booksendform()
            messages.success(request, 'Form submission successful')
            ctx['mybooksend'] = Book.objects.filter(user=request.user).order_by('-publish')
            return render(request, 'send.html', ctx)
    else:
        ctx['form'] = form = Booksendform()
        ctx['mybooksend'] = Book.objects.filter(user=request.user).order_by('-publish')
    return render(request, 'send.html', ctx)
