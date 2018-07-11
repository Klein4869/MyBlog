from django.urls import path
from . import views as indexSiteViews

urlpatterns=[
    path('', indexSiteViews.index)
]