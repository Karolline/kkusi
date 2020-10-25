from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.reindex, name='reindex'),
    
    path('intro_adopt/', views.intro_adopt, name='intro_adopt'),
    path('intro1/', views.intro1, name='intro1'),
    path('intro2/', views.intro2, name='intro2'),
    path('intro3/', views.intro3, name='intro3'),
    
    path('cands/', views.cands, name='cands'),
    path('cand/<int:cand_id>/', views.cand, name='cand'),
    path('posts/', views.posts, name='posts'),
    
    
]