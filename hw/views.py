from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time
import random

# Create your views here.
def home(request):
    response_text = f'''
    <html>
    <h1>Hello, World!</h1>
    The current time is: {time.ctime()}.
    </html>
    '''
    return HttpResponse(response_text)

def home_page(request):
    template_name = 'hw/home.html'
    context = {
        'time': time.ctime(),
        'letter1': chr(random.randint(65, 90)),
        'letter2': chr(random.randint(65, 90)),
        'number': random.randint(0, 10),
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'hw/about.html'
    context = {
        'time': time.ctime(),
        'letter1': chr(random.randint(65, 90)),
        'letter2': chr(random.randint(65, 90)),
        'number': random.randint(0, 10),
    }
    return render(request, template_name, context)