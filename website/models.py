from django.db import models

def image_path(instance, filename):
        from random import choice
        import string
        
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr)
        extension = filename.split('.')[-1]
        
        return 'images/%s.%s' % (pid, extension)
        
GENDER_CHOICES = (
        ('M', '남'),
        ('F', '여')
    )
        
class Protector(models.Model):
    name = models.CharField(max_length=10)
    
    naver_id = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=11, null=True)
    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(null=True)
    memo = models.TextField(null=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "임시보호자"

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    # kind = models.CharField(
    birth_year = models.IntegerField()
    
    adopted = models.BooleanField()
    protector = models.ForeignKey(Protector, on_delete=models.SET_NULL, null=True)
    
    image = models.ImageField(upload_to=image_path)
    
    reg_date = models.DateTimeField(auto_now_add = True)
    
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
    mod_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "입양 홍보글"
    
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=image_path)