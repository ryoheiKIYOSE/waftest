from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import Message
from .forms import MessageForm

class MessageList(generic.ListView):
    model = Message
    template_name = "post/index.html"

class MessageCreate(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = "post/post.html"
    success_url = reverse_lazy('index')