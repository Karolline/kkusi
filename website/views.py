from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

def list(request):
    candidates = Candidate.objects.all()
    str = ""
    
    for candidate in candidates:
        str += "{}<br>{}".format(candidate.title, candidate.name)
        
    str += '<br>'
    return HttpResponse(str)
    
def index(request):
    return render(request, 'website/index.html', {})

# Create your views here.
