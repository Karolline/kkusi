from django.db import models

def image_path(instance, filename):
        from random import choice
        import string
        
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr)
        extension = filename.split('.')[-1]
        
        return 'images/%s.%s' % (pid, extension)

class Candidate(models.Model):

    GENDER_CHOICES = (
        ('M', '남아'),
        ('F', '여아')
    )
    
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    # kind = models.CharField(
    birth_year = models.IntegerField()
    
    adopted = models.BooleanField()
    
    image = models.ImageField(upload_to=image_path)
    
    reg_date = models.DateTimeField(auto_now_add = True)
    
    def register(self):
        self.save()
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "토끼 목록"
        
# class User(models.Model):
    
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='알 수 없는 사용자')
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    cand = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True)
    
    hide_yn = models.BooleanField()
    
    pub_date = models.DateTimeField(auto_now_add = True)
    mod_date = models.DateTimeField()
    
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=image_path)