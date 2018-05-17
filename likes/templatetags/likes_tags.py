from django import template
from likes import services 
from django.urls import reverse
register = template.Library()

@register.filter
def get_likes(obj):
	return services.get_likes_count(obj)
	
@register.filter
def likes_url(obj,user):
	if services.has_liked(obj,user):
		return reverse("remove_like",args = [obj.slug])
	return reverse("add_like",args = [obj.slug])
	
@register.filter
def is_liked(obj, user):
	if services.has_liked(obj,user):
		return "i_like"
	return ""
	