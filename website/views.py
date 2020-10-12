from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Post
    
def index(request):
    return render(request, 'website/index.html')
    
def cands(request):
    candidates = Candidate.objects.filter(adopted='False')
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