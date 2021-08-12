from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Hitokoto
from django.urls import reverse
from .forms import HitokotoForm
from django.urls import reverse_lazy


class Message_List(ListView):
    template_name = 'comment_list.html'
    model = Hitokoto


class Message_detail(DetailView):
    model = Hitokoto
    template_name = 'comment_detail.html'
    context_object_name = 'message'


class Message_Post(CreateView):
    model = Hitokoto
    form_class = HitokotoForm
    template_name = 'Hitokoto_post.html'
    fields = ('name', 'comment',)
    success_url = reverse_lazy('comments')
