from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post 





# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset[:3]

class PostListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(image__isnull=False).order_by("-date")

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"


