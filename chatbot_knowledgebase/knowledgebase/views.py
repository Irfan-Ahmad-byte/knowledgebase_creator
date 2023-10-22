from django.shortcuts import render

# Create your views here.

# a django rest framework view to render the index.html template
def index(request):
    return render(request, 'index.html')


