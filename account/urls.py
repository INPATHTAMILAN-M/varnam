from django.urls import path
from rest_framework.routers import DefaultRouter
from account.viewsets.register import RegisterViewSet
from account.viewsets.auth import LoginView
from account.viewsets.password_reset import PasswordResetRequestView, PasswordResetConfirmView

app_name = 'account'

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]

urlpatterns += router.urls
