from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import GPost
from django.urls import reverse_lazy
from .forms import PostForm


# Create your views here.

class GalleryPageView(ListView):
    model = GPost
    template_name = 'gallery/gallery_home.html'


class CreatePostView(CreateView):
    model = GPost
    form_class = PostForm
    template_name = 'gallery/gallery_post.html'
    success_url = reverse_lazy('gallery-home')
