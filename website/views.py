from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
    
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'website/index.html', context)