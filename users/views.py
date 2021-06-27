from django.http import HttpResponse
from django.shortcuts import render
from users.models import SubscribedUser
from users.serializers import SubscribedUserSerializer
from users.forms import SubscribeForm
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# def subscription_page(request, *args, **kwargs):
# 	print(args, kwargs)
# 	print(request.user)
# 	context = {"name": "ambili", "age": 26, "list": [1,2,3,4]}
# 	return render(request, "home.html", context)
	# return HttpResponse("<h1>Hello World</h1>")

def create(request):
	form = SubscribeForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {'form': form}
	return render(request, "create.html", context)

def subscribed_list(request):
	query_set = SubscribedUser.objects.all()
	context = {'object_list': query_set}
	return render(request, "subscribed_list.html", context)
