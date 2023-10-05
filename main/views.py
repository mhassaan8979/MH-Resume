from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, "main/home.html", context)

def contact(request):
    context = {'contact': 'active'}
    return render(request, "main/contact.html", context)