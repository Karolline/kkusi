from django.contrib import admin
from .models import Candidate, Post, Photo, Protector

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'adopted', 'image', 'protector', )
    list_editable = ('adopted', )
    list_filter = ('adopted', )
    search_fields = ('name', )
    
    fieldsets = (
        ('기본 정보', {'fields': (('name', 'gender', 'age',))}),
        ('입양 여부', {'fields': (('protector', 'adopted',))}),
        ('썸네일', {'fields': (('image', ))})
    )
    
admin.site.register(Candidate, CandidateAdmin)

class PhotoInline(admin.TabularInline):
    model = Photo
    
class ProtectorAdmin(admin.ModelAdmin):
    fieldsets = (
            ('기본 정보', {'fields': (('name', 'naver_id', 'phone_number',))}),
            ('신상 정보', {'fields': (('gender', 'age',))}),
            ('참고 사항', {'fields': (('memo', ))})
        )

admin.site.register(Protector, ProtectorAdmin)

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Post, PostAdmin)