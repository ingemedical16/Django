from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts", views.PostListView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later")
]
