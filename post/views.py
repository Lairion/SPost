from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .forms import PostForm
from .models import Post
from likes import services

class PostViews(object):
    """docstring for PostViews"""
    @staticmethod
    def post_create(request):
        print('\n'.join(dir(request.user)))
        if not request.user.is_authenticated:
            messages.error(request, "Please, login in your account")
            return redirect("posts_list")
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # message success
            messages.success(request, "Successfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
            "form": form,
        }
        return render(request, "post_form.html", context)

    @staticmethod
    def post_detail(request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        context = {
            "title": instance.title,
            "instance": instance,
        }
        return render(request, "post_details.html", context)

    @staticmethod
    def post_list(request):
        queryset_list = Post.objects.order_by("-timestamp")
        if request.user.is_staff or request.user.is_superuser:
            queryset_list = Post.objects.all()
        
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        paginator = Paginator(queryset_list, 3)
        page = request.GET.get("page")
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)


        context = {
            "object_list": queryset, 
            "title": "Post",
        }
        return render(request, "post_list.html", context)

    @staticmethod
    def post_update(request, slug=None):
        instance = get_object_or_404(Post, slug=slug)
        if not request.user.is_authenticated:
            messages.error("You can't update this post")
            return HttpResponseRedirect(instance.get_absolute_url())
        if instance.user == request.user:
            form = PostForm(request.POST or None, request.FILES or None, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
                return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request, "<a href='#'>Item</a> no saved. Access denied", extra_tags='html_safe')
        context = {
            "title": instance.title,
            "instance": instance,
            "form":form,
        }
        return render(request, "post_form.html", context)

    @staticmethod
    def post_delete(request, slug=None):
        if not request.user.is_authenticated:
            messages.error(request, "Please, login in your account")
        else:
            instance = get_object_or_404(Post, slug=slug)
            if (instance.user == request.user) or request.user.is_staff:
                instance.delete()
                messages.success(request, "Successfully deleted")
            else:
               messages.error(request, "Item not delete. Access denied") 
        return redirect("posts_list")

    