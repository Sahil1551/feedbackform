from django.urls import path

from . import views

app_name = 'details'
urlpatterns = [
    path('', views.feedback_form, name='home'),
]