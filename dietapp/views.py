from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, DietEntryForm
from .models import DietEntry

def home_view(request):
    return render(request, "home.html")  # You need to create a template for this

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

@login_required
def dashboard_view(request):
    diet_entries = DietEntry.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"diet_entries": diet_entries})

@login_required
def diet_questionnaire_view(request):
    if request.method == "POST":
        form = DietEntryForm(request.POST)
        if form.is_valid():
            diet_entry = form.save(commit=False)
            diet_entry.user = request.user
            diet_entry.save()
            return redirect("dashboard")
    else:
        form = DietEntryForm()
    return render(request, "diet_questionnaire.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
