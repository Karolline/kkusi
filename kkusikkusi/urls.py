"""from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path(r'', include('website.urls')),
    path('admin/', admin.site.urls)
]
