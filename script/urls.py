from django.urls import path

from . import views

app_name = 'script'

urlpatterns = [
    path('', views.ScriptTop.as_view(), name='top')
]
