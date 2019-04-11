from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event, Comment
from .forms import CommentForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['event_name', 'venue', 'time', 'fee', 'date', 'description', 'contact', 'cover']


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['event_name', 'venue', 'time', 'fee', 'date', 'description', 'contact', 'cover']


class EventDeleteView(DeleteView):
    model = Event
    success_url = '/'


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comment = Comment.objects.all()
    return render(request, 'showcase/detail.html', {'event': event, 'comment': comment})


def create_comment(request, event_id):
    form = CommentForm(request.POST or None)
    event = get_object_or_404(Event, pk=event_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.event = event
        comment.save()
    return render(request, 'showcase/create_comment.html', {'form': form})


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('showcase:event-index')
    return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('showcase:event-index')
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('showcase:login')

