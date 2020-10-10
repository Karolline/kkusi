from django.db import models

class Candidate(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    def user_path(instance, filename):
        from random import choice
        import string
        
        arr = [choice(string.ascii_letters) for _ in range(8)]
        pid = ''.join(arr)
        extension = filename.split('.')[-1]
        
        return 'website/photo/%s.%s' % (pid, extension)
    
    # user = models.ForeignKey
    title = models.CharField(max_length=30)
    # content
    
    # kind = models.CharField(
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    name = models.CharField(max_length=10)
    
    image = models.ImageField(upload_to = user_path)
    # thumname_image = 
    
    reg_date = models.DateTimeField(auto_now_add = True)
    
    def register(self):
        self.save()
    
    def __str__(self):
        return self.name
    
