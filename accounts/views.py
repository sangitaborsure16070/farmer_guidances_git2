from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .forms import FarmerRegistrationForm, FarmerProfileForm
from .models import FarmerProfile, District, Taluka, Village

def register_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["mobile_number"]
            if User.objects.filter(username=username).exists():
                messages.error(request, _("A user with this mobile number already exists."))
                return render(request, "accounts/register.html", {"form": form})

            user = User.objects.create_user(
                username=username,
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"]
            )

            profile = form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, _("Registration successful! Welcome to KisanMitra."))
            return redirect("core:home")
    else:
        form = FarmerRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _("Welcome back!"))
            return redirect("core:home")
        else:
            messages.error(request, _("Invalid username/mobile number or password."))
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, _("You have logged out successfully."))
    return redirect("core:home")

@login_required
def profile_view(request):
    profile, created = FarmerProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = FarmerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user = request.user
            user.first_name = request.POST.get("first_name", user.first_name)
            user.last_name = request.POST.get("last_name", user.last_name)
            user.email = request.POST.get("email", user.email)
            user.save()

            form.save()
            messages.success(request, _("Profile updated successfully."))
            return redirect("accounts:profile")
    else:
        form = FarmerProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {"form": form, "profile": profile})

# AJAX Location Endpoints
def load_districts(request):
    state_id = request.GET.get("state_id")
    if not state_id or not str(state_id).isdigit():
        return JsonResponse([], safe=False)
    districts = District.objects.filter(state_id=int(state_id)).order_by("name").values("id", "name", "name_mr")
    return JsonResponse(list(districts), safe=False)

def load_talukas(request):
    district_id = request.GET.get("district_id")
    if not district_id or not str(district_id).isdigit():
        return JsonResponse([], safe=False)
    talukas = Taluka.objects.filter(district_id=int(district_id)).order_by("name").values("id", "name", "name_mr")
    return JsonResponse(list(talukas), safe=False)

def load_villages(request):
    taluka_id = request.GET.get("taluka_id")
    if not taluka_id or not str(taluka_id).isdigit():
        return JsonResponse([], safe=False)
    villages = Village.objects.filter(taluka_id=int(taluka_id)).order_by("name").values("id", "name", "name_mr")
    return JsonResponse(list(villages), safe=False)