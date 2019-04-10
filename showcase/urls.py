from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-index'),
    path('create_event', views.EventCreateView.as_view(), name='create-event'),
    path('<int:pk>/update-event', views.EventUpdateView.as_view(), name='update-event'),
    path('<int:pk>/delete-event', views.EventDeleteView.as_view(), name='delete-event'),
    path('(?P<event_id>[0-9]+)/', views.detail, name='detail'),
]
