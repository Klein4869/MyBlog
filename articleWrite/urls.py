from django.urls import path
from . import views as writeViews

urlpatterns = [
    path('article/', writeViews.articleWritePageInitial, name='articleWritePageInitial')
]