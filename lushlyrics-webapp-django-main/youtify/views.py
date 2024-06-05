from    django.shortcuts import render
from    rest_framework import status
from    rest_framework.response import Response
from    django.views import View
from    allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from    dj_rest_auth.registration.views import RegisterView
from    dj_rest_auth.views import LoginView
from    allauth.account.views import ConfirmEmailView
from    dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from    django.utils.decorators import method_decorator
from    django.views.decorators.csrf import csrf_exempt

class CustomRegisterView(RegisterView):
    template_name = 'signup.html'
    def get(self, request):
        return render(request, self.template_name)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)

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