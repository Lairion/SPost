from django.urls import path
from .views import AuthViews

urlpatterns = [
    path('auth/',AuthViews.auth, name="sign_up"),
    path('sign_up/',AuthViews.sign_up, name="sign_up"),
    path('sign_in/',AuthViews.sign_in, name="sign_in")
]
