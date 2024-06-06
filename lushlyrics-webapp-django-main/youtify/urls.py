from    django.contrib import admin
from    django.urls import path, include
from    .views import CustomLoginView
from    .views import CustomRegisterView
from    dj_rest_auth.registration.views import VerifyEmailView
from    dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from    .views import CustomConfirmEmailView, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/login/', CustomLoginView.as_view(), name='custom_login'),
    path('auth/logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('auth/password/reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/account-confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('auth/register/', CustomRegisterView.as_view(), name='custom_register'),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
]
