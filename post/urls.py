from django.urls import path
from .views import PostViews

urlpatterns = [
    path('posts_list/', PostViews.post_list, name='posts_list'),
    path('posts_list_json/', PostViews.posts_list_json, name='posts_list_json'),
    path('posts_list/create/', PostViews.post_create),
    path('posts_list/<str:slug>/', PostViews.post_detail, name='post_detail'),
    path('posts_list/<str:slug>/edit/', PostViews.post_update, name='post_update'),
    path('posts_list/<str:slug>/delete/', PostViews.post_delete),
]