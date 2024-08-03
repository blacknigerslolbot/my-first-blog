from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reguest):
    return render(reguest, 'blog/index.html', {})

def categ(reguest):
    return HttpResponse('<h1>page1</h1>')
