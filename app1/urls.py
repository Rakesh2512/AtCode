from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('Problem', views.problemset, name='problemset'),
    path('contest', views.contest, name='contest'),
    path('profile', views.profile, name='profile'),
    path('ds1', views.data, name='Data-Structure'),
    path('algo', views.algo, name='Algorithm'),
    path('editor', views.editor, name='Editor'),
    path('register',views.register, name='Register')
]
