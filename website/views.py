from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Post
from .models import GENDER_CHOICES, CANDS_STATUS
    
def index(request):
    return render(request, 'website/index.html')
    
def reindex(request):
    return redirect(index)
    
def cands(request):
    candidates = Candidate.objects.exclude(adopted__in=['3', '4'])
    
    for cand in candidates:
        if cand.gender == 'M':
            cand.gender = '남아'
        elif cand.gender == 'F':
            cand.gender = '여아'
            
        if cand.adopted is not None:
            cand.adopted = CANDS_STATUS[int(cand.adopted)-1][1]
            
        if cand.neutering == 'True':
            cand.neutering = 'O'
        elif cand.neutering == 'False':
            cand.neutering = 'X'
        else:
            cand.neutering = ''
            
    
    return render(request, 'website/cands.html', {'candidates': candidates})
    
def cand(request, cand_id):
    cand = Candidate.objects.get(id=cand_id)
    # posts = get_object_or_404(Post, cand=cand_id)
    posts = Post.objects.filter(cand=cand_id)
    return render(request, 'website/cand.html',  {'cand': cand, 'posts': posts})
    
def posts(request):
    posts = Post.objects.all()
    return render(request, 'website/posts.html', {'posts': posts})
    
def notice(request):
    return render(request, 'website/notice.html')