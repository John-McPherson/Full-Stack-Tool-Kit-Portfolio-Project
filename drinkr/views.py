from django.shortcuts import render

# from django.views import generic

def home_page(request):
    return render(request, '../templates/index.html')
