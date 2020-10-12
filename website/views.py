from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
    
def index(request):
    return render(request, 'website/index.html')
    
def cands(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'website/cands.html', context)