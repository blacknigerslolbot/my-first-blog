from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reguest):
    return render(reguest, 'blog/index.html', {})

def categ(reguest, catid):
    return HttpResponse(f'<h1>Число {catid}</h1>')