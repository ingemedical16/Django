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
        return render(request, self.template_name, self.get_context(request,post, comment_form))

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)

        # If form invalid, render with same context but filled-in form
        return render(request, self.template_name, self.get_context(request,post, comment_form))

    def get_context(self,request, post, comment_form):
        stored_posts = request.session.get("stored_posts")
        is_saved_for_later = False
        if stored_posts is not None:
            is_saved_for_later = post.id in stored_posts
        return {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": is_saved_for_later
        }

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)   
            
        request.session["stored_posts"] = stored_posts
            
        return redirect("index")