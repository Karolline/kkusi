from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.reindex, name='reindex'),
    path('cands/', views.cands, name='cands'),
    path('cand/<int:cand_id>/', views.cand, name='cand'),
    path('posts/', views.posts, name='posts'),
    path('notice/', views.notice, name='notice'),
]