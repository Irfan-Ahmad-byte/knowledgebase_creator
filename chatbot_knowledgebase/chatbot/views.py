from django.shortcuts import render

# Create your views here.



# a django rest framework view to render the chatbot.html template
def chatbot(request):
    return render(request, 'chatbot.html')