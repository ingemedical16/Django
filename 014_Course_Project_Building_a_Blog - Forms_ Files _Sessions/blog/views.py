from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.base import View
from django.shortcuts import redirect


from .models import Post 
from .forms import CommentForm





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

class PostDetailView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm()
        return render(request, self.template_name, self.get_context(post, comment_form))

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)

        # If form invalid, render with same context but filled-in form
        return render(request, self.template_name, self.get_context(post, comment_form))

    def get_context(self, post, comment_form):
        return {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date")
        }

class ReadLaterView(View):
    def post(self, request):
        pass