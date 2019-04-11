from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'showcase'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.EventListView.as_view(), name='event-index'),
    path('create_event', views.EventCreateView.as_view(), name='create-event'),
    path('(?P<event_id>[0-9]+)/create_comment', views.create_comment, name='create-comment'),
    path('<int:pk>/update-event', views.EventUpdateView.as_view(), name='update-event'),
    path('<int:pk>/delete-event', views.EventDeleteView.as_view(), name='delete-event'),
    path('(?P<event_id>[0-9]+)/', views.detail, name='detail'),
    path('(?P<event_id>[0-9]+)/new-comment', views.create_comment, name='create-comment'),
]
