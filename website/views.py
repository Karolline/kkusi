from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Post, Photo
from .models import GENDER_CHOICES, CANDS_STATUS
    
def index(request):
    return render(request, 'website/index.html')
    
def reindex(request):
    return redirect(index)
        
def intro1(request):
    return render(request, 'website/intro1.html')
    
def intro2(request):
    return render(request, 'website/intro2.html')
    
def intro3(request):
    return render(request, 'website/intro3.html')

def intro_adopt(request):
    return render(request, 'website/intro_adopt.html')
    
def convert_cand(candidates):
    for cand in candidates:
        if cand.gender == 'M':
            cand.gender = '남아'
        elif cand.gender == 'F':
            cand.gender = '여아'
            
        if cand.adopted is not None:
            cand.adopted = CANDS_STATUS[int(cand.adopted)-1][1]
            
        if cand.neutering is True:
            cand.neutering = 'O'
        elif cand.neutering is False:
            cand.neutering = 'X'
        else:
            cand.neutering = '미상'
            
    return candidates

def cands(request):
    candidates = Candidate.objects.exclude(adopted__in=['3', '4'])
    candidates = convert_cand(candidates)
    
    return render(request, 'website/cands.html', {'candidates': candidates})
    
def cand(request, cand_id):
    cand = Candidate.objects.get(id=cand_id)
    cand = convert_cand([cand])[0]
    
    posts = Post.objects.filter(cand=cand_id)
    
    # photos = Photo.objects.select_related('post').filter(post_id__in=post_id)
    # photos = Photo.objects.filter(post__in=posts)
    
    post_sets = []
    
    for post in posts:
        test = {}
        test['post'] = post
        test['photos'] = Photo.objects.filter(post = post)
        post_sets.append(test)
    
    print(post_sets)

    return render(request, 'website/cand.html',  {'cand': cand, 'post_sets': post_sets})
    
def posts(request):
    posts = Post.objects.all()
    return render(request, 'website/posts.html', {'posts': posts})
    
