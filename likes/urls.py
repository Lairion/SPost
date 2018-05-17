from django.urls import path
from .views import LikesViews

urlpatterns = [
    path('remove_like/<str:slug>',LikesViews.remove_like, name="remove_like"),
    path('add_like/<str:slug>',LikesViews.add_like, name="add_like")
]