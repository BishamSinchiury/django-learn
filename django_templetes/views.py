from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Bisham',
        'age': 20,
        'hobbies': ['Coding', 'Reading', 'Gaming']
    }
    return render(request, 'myapp/home.html', context)
