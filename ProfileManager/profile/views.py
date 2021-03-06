from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def home(request):
    return render_to_response("home.html",
                              {},
                              context_instance = RequestContext(request))

def login(request):
    return render_to_response("login.html",
                              {},
                              context_instance = RequestContext(request))

def signup(request):
    return render_to_response("signup.html",
                              {},
                              context_instance = RequestContext(request))

@login_required
def profile(request):
    return render_to_response("profile.html",
                              {},
                              context_instance = RequestContext(request))

