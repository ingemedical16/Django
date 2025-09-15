from django.urls import path

from  . import views
urlpatterns = [
path("",views.ReviewListView.as_view(), name='review_list'),
path("add-review",views.ReviewView.as_view(), name='add_review'),
path("thank-you",views.ThankYouView.as_view(), name='thank_you'),

path("reviews/<int:pk>",views.SingleReviewView.as_view(), name='review_detail'),
]