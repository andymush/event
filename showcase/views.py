from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Event, Comment
from .forms import CommentForm

# Create your views here.


class EventListView(ListView):
    model = Event
    context_object_name = 'events'


class EventCreateView(CreateView):
    model = Event
    fields = ['event_name', 'venue', 'time', 'fee', 'date', 'description', 'contact', 'cover']


class EventUpdateView(UpdateView):
    model = Event
    fields = ['event_name', 'venue', 'time', 'fee', 'date', 'description', 'contact', 'cover']


class EventDeleteView(DeleteView):
    model = Event
    success_url = '/'


def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'showcase/detail.html', {'event': event})


def create_comment(request, event_id):
    form = CommentForm(request.POST or None)
    event = get_object_or_404(Event, pk=event_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.event = event
        comment.save()
    return render(request, 'showcase/detail.html', {'form':form})

