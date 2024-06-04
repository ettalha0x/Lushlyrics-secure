from    django.shortcuts import render
from    django.views import View
from    allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from    dj_rest_auth.registration.views import RegisterView
from    dj_rest_auth.views import LoginView
# from    dj_rest_auth.registration.views import VerifyEmailView
from    allauth.account.views import ConfirmEmailView
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

# class CustomConfirmEmailView(VerifyEmailView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 200:
#             return render(request, 'email_verification_success.html')
#         else:
#             return render(request, 'email_verification_fail.html')

@method_decorator(csrf_exempt, name='dispatch')
class CustomConfirmEmailView(ConfirmEmailView):
    template_name = 'confirm_email.html'

    def get(self, request, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(request)
        return render(request, self.template_name, self.get_context_data())
    