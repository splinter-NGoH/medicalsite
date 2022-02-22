from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext_lazy as _

def home (request):
    # this is a test translate
    output = _("Welcome to my site.")
    output1 = _("Wniceone")

    return render(request, 'home.html', {"output": output, "output1":output1})