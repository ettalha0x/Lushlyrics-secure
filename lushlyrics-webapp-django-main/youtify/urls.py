from    django.contrib import admin
from    django.urls import path, include
from    .views import CustomLoginView
from    .views import CustomRegisterView
from    dj_rest_auth.registration.views import VerifyEmailView
from    .views import CustomConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/login/', CustomLoginView.as_view(), name='custom_login'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/account-confirm-email/<str:key>/', CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    path('auth/register/', CustomRegisterView.as_view(), name='custom_register'),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
]
