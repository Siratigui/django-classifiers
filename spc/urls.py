# -*- coding: utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mnnb', views.mnnb, name='mnnb'),
    path('post_mnnb', views.post_mnnb, name='post_mnnb'),
    
    path('lreg', views.lreg, name='lreg'),
    path('post_lreg', views.post_lreg, name='post_lreg'),
    
    path('svm', views.svm, name='svm'),
    path('post_svm', views.post_svm, name='post_svm'),
    
    path('nltk', views.nltk, name='nltk'),
    path('post_nltk', views.post_nltk, name='post_nltk'),
]