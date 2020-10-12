from django.db import models

class Candidate(models.Model):

    GENDER_CHOICES = (
        ('M', '남아'),
        ('F', '여아')
    )
    
    def user_path(instance, filename):
        from random import choice
        import string
        
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr)
        extension = filename.split('.')[-1]
        
        return 'images/%s.%s' % (pid, extension)
    
    # kind = models.CharField(
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    name = models.CharField(max_length=10)
    # adopted
    
    image = models.ImageField(upload_to=user_path)
    
    reg_date = models.DateTimeField(auto_now_add = True)
    
    def register(self):
        self.save()
    
    def __str__(self):
        return self.title
        
class User(models.Model):
    
    
class Post(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='알 수 없는 사용자')
    
    cand = models.ForeignKey(Candidate, on_delete=models.SET_NULL)
    
    pub_date = models.DateTimeField(auto_now_add = True)