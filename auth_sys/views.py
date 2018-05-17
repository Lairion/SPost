from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User# Create your views here.
class AuthViews:
    @staticmethod
    def sign_in(request):
        post_obj = request.POST
        user = authenticate(request, username=post_obj.get('username'), password=post_obj.get('password'))
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("posts_list")
        messages.error("Your login or password is wrong")
        # Return an 'invalid login' error message.
        return redirect("auth")

    @staticmethod
    def sign_up(request):
        post_obj = request.POST
        if post_obj.get("password") == post_obj.get("conf-password"):
            user = User.objects.create_user(
                post_obj.get("username"),
                post_obj.get("email"),
                post_obj.get("password"))
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect("posts_list")
        messages.error("Your data incorrect, please sign up again")
            # Return an 'invalid login' error message.
        return redirect("auth")

    def auth(request):
        context = {
            'title':'Auth'
        }
        return render(request,'auth.html',context)

    



            


    
