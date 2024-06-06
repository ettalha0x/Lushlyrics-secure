from    django.shortcuts import render, redirect
from    rest_framework import status
from    rest_framework.response import Response
from    main.models import playlist_user
from    django.views import View
from    dj_rest_auth.registration.views import RegisterView
from    dj_rest_auth.views import LoginView, LogoutView
from    allauth.account.views import ConfirmEmailView
from    dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

from    django.utils.decorators import method_decorator
from    django.views.decorators.csrf import csrf_exempt

class CustomRegisterView(RegisterView):
    template_name = 'signup.html'
    def get(self, request):
        return render(request, self.template_name)

    def perform_create(self, serializer):
        user = super().perform_create(serializer)
        playlist_user.objects.create(username=user.username)
        return user

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response['Location'] = '/'
            response.status_code = status.HTTP_302_FOUND
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            response['Location'] = '/auth/register/'
            response.status_code = status.HTTP_302_FOUND
        return response

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, self.template_name)

    def get_response(self):
        response = super().get_response()
        if response.status_code == status.HTTP_200_OK:
            response['Location'] = '/'
            response.status_code = status.HTTP_302_FOUND
        else:
            response['Location'] = '/auth/login/'
            response.status_code = status.HTTP_302_FOUND
        return response

@method_decorator(csrf_exempt, name='dispatch')
class CustomConfirmEmailView(ConfirmEmailView):
    template_name = 'confirm_email.html'

    def get(self, request, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(request)
        return render(request, self.template_name, self.get_context_data())

@method_decorator(csrf_exempt, name='dispatch')
class   CustomPasswordResetView(PasswordResetView):
    template_name = 'pwd_reset.html'
    def get(self, request):
        return render(request, self.template_name)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'pwd_reset_confirm.html'
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token,
        }
        return render(request, self.template_name, context)

class CustomLogoutView(LogoutView):
    def post(self, request):
        self.logout(request)
        return redirect('/auth/login/')