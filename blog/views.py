from django.shortcuts import render,get_object_or_404
from .models import Blog

def home(request):
    blogs=Blog.objects
    return render(request,'blog/blog_home.html',{'blogs':blogs})

def details(request,blog_id):
    details=get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/details.html', {'details':details})
