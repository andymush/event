from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-index'),
]
