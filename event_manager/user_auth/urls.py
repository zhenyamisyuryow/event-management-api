from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register-view'),

    # I will use the default views provided by the rest_framework_simplejwt for user authentication
    path('token/obtain', TokenObtainPairView.as_view(), name='token-obtain-pair-view'),
    path('token/refresh', TokenRefreshView.as_view(), name='token-refresh-view')
]
