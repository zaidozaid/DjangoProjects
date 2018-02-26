from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,UpdateView,CreateView)
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm,CommentForm
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post


    def get_queryset(self):
        return Post.objects.filter(published_date__lte=time.now().order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post


class CreateView(LoginRequiredMixin,CreateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class =PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class =PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin,DetailView):
    model = Post
    success_url = reverse_lazy("post_list")




class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'



    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')






