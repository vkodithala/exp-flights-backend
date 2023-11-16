from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    my_data = "Hello, world!"

    context = {
        'my_data': my_data,
    }

    return render(request, 'index.html', context=context)
