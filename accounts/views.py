from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib import messages

from django.core.mail import EmailMessage

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import UserProfile

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# class SignupPageView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"


def SignupPageView(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # phone = form.cleaned_data["phone"]
            # email = form.cleaned_data["email"]
            request.session["username"] = form.cleaned_data["username"]
            request.session["email"] = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if password1 != password2:
                messages.error(request, "Password mismatch")
                return redirect("signup")

            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("home")
    else:
        initial = {
            "username": request.session.get("username", ""),
            "email": request.session.get("email", ""),
        }
        form = CustomUserCreationForm(initial=initial)

    return render(
        request,
        "registration/signup.html",
        {
            "form": form,
        },
    )


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = UserProfile.objects.filter(Q(email=data))
            if associated_users.exists():

                for user in associated_users:
                    subject = "Password Reset Requested"
                    current_site = get_current_site(request)

                    email_template_name = "registration/password_reset_email.html"
                    c = {
                        "email": user.email,
                        "domain": current_site,
                        "site_name": "ASLPathology",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_email = EmailMessage(subject, email, to=[user.email])
                        send_email.send()

                    except BadHeaderError:

                        return HttpResponse("Invalid header found.")

                    messages.success(
                        request,
                        "A message with reset password instructions has been sent to your inbox.",
                    )
                    return redirect("password_reset_done")
                else:
                    messages.error(request, "Account does not exist!")
                    return redirect("password_reset")

    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="registration/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )
