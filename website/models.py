from django.db import models

def image_path(instance, filename):
    from random import choice
    import string
    
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    
    return 'images/%s.%s' % (pid, extension)
        
PROTECTOR_CHOICES = (
    ('1', '임시보호자'),
    ('2', '입양자'),
    ('3', '임보&입양자'),
    ('4', '기타')
)        

GENDER_CHOICES = (
    ('M', '남'),
    ('F', '여'),
    ('Q', '미상'),
)

CANDS_STATUS = (
    ('1', '보호중'),
    ('2', '가정임보중'),
    ('3', '입양예약'),
    ('4', '입양완료')
)
        
class Protector(models.Model):
    name = models.CharField(max_length=10, verbose_name='이름')
    type = models.CharField(max_length=2, choices=PROTECTOR_CHOICES, null=True, blank=True, verbose_name='보호타입')
    
    phone_number = models.CharField(max_length=11, null=True, blank=True, verbose_name='전화번호')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='주소')
    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='성별')
    age = models.IntegerField(null=True, blank=True, verbose_name='나이')
    memo = models.TextField(null=True, blank=True, verbose_name='기타 메모')
    
    naver_id = models.CharField(max_length=20, null=True, blank=True, verbose_name='네이버 ID')
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='닉네임')
    insta_id = models.CharField(max_length=20, null=True, blank=True, verbose_name='인스타 ID')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "보호자"

class Candidate(models.Model):
    name = models.CharField(max_length=10, verbose_name='이름')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='성별')
    kind = models.CharField(max_length=20, null=True, blank=True, verbose_name='종')
    # birth_year = models.IntegerField(null=True, , verbose_name='')
    age = models.CharField(max_length=20, blank=True, verbose_name='나이')
    neutering = models.BooleanField(null=True, blank=True, verbose_name='중성화 여부')
    
    # adopted = models.BooleanField(verbose_name='입양완료여부')
    adopted = models.CharField(max_length=2, choices=CANDS_STATUS, null=True, blank=True, verbose_name='보호상태')
    protector = models.ForeignKey(Protector, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='보호자')
    
    image = models.ImageField(upload_to=image_path, null=True, blank=True, verbose_name='대표사진')
    
    reg_date = models.DateTimeField(auto_now_add = True, verbose_name='등록일자')
    adopt_date = models.DateTimeField(null=True, blank=True, verbose_name='입양날짜')
    
    memo = models.TextField(null=True, blank=True, verbose_name='기타 메모')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "토끼 목록"
        
# class User(models.Model):
    
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='알 수 없는 사용자')
    title = models.CharField(max_length=30, verbose_name='제목')
    content = models.TextField(verbose_name='내용', null=True, blank=True)
    
    cand = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='토끼')

    hide_yn = models.BooleanField(verbose_name='숨김여부')

    pub_date = models.DateTimeField(auto_now_add = True, verbose_name='등록날짜')
    mod_date = models.DateTimeField(auto_now_add = True, verbose_name='수정날짜')
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "입양 홍보글"
    
class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)