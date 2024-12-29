from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('savejump.urls')),
    path('savejump/', include('savejump.urls')),
    path('admin/', admin.site.urls),
]

