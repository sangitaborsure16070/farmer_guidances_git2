from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Farm, Crop
from .forms import FarmForm, CropForm

@login_required
def farm_list_view(request):
    farms = Farm.objects.filter(user=request.user).prefetch_related("crops")
    return render(request, "farms/farm_list.html", {"farms": farms})

@login_required
def farm_detail_view(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)
    crops = farm.crops.all()
    return render(request, "farms/farm_detail.html", {"farm": farm, "crops": crops})

@login_required
def farm_add_view(request):
    if request.method == "POST":
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user
            farm.save()
            messages.success(request, _("Farm added successfully!"))
            return redirect("farms:farm_detail", farm_id=farm.id)
    else:
        form = FarmForm()

    return render(request, "farms/farm_form.html", {"form": form, "title": _("Add New Farm")})

@login_required
def farm_edit_view(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)
    if request.method == "POST":
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            messages.success(request, _("Farm details updated."))
            return redirect("farms:farm_detail", farm_id=farm.id)
    else:
        form = FarmForm(instance=farm)

    return render(request, "farms/farm_form.html", {"form": form, "title": _("Edit Farm"), "farm": farm})

@login_required
def crop_add_view(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id, user=request.user)
    if request.method == "POST":
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farm = farm
            crop.save()
            messages.success(request, _("Crop added to farm successfully!"))
            return redirect("farms:farm_detail", farm_id=farm.id)
    else:
        form = CropForm()

    return render(request, "farms/crop_form.html", {"form": form, "farm": farm})