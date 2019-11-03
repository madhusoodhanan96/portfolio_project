from django.shortcuts import render

def homepage(request):
    return render(request, 'job/homepage.html')

def home(request):
    return render(request, 'job/job_home.html')
