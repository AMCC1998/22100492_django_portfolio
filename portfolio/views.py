from django.shortcuts import render

# Create your views here.

#  hello/views.py


def home_page_view(request):
    return render(request, 'portfolio/home.html')
