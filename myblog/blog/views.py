from django.shortcuts import render
from core.models import *

# Create your views here.
def home(request):
    posts = post.objects.filter(status=post.ACTIVE)
    return render(request,'blog/home.html',{'posts':posts})


def about(request):
    return render(request, 'blog/about.html')