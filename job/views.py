from django.shortcuts import render


def home(request):
    return render(request, 'job/job_home.html')

def about(request):
    return render(request, 'job/about.html')
