from django.urls import path

from . import views

app_name = 'script'

urlpatterns = [
    path('top/', views.ScriptTop.as_view(), name='top'),
    path('predict/', views.ScriptPredict.as_view(), name='predict'),
    path('label/<str:slug>/', views.ScriptLabel.as_view(), name='label')
]
