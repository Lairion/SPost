from likes import services
from django.shortcuts import get_object_or_404, redirect
from post.models import Post

class LikesViews:

    @staticmethod
    def remove_like(request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        services.remove_like(instance,request.user )
        return redirect("posts_list")

    @staticmethod
    def add_like(request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        services.add_like(instance,request.user )
        return redirect("posts_list")