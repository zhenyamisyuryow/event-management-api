from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('events.urls')),
    path('api/v1/auth/', include('user_auth.urls')),
]