from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def problemset(request):
    return render(request, 'problemset.html')


def contest(request):
    return render(request, 'contest.html')


def profile(request):
    return render(request, 'profile.html')


def data(request):
    return render(request, 'ds1.html')


def algo(request):
    return render(request, 'algo.html')


def editor(request):
    return render(request, 'ds.html')


def register(request):
    return render(request, 'register.html')
