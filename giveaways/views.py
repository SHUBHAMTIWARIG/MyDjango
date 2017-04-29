# Create your views here.
from django.contrib import messages
from django.shortcuts import render

from giveaways.form import giveaway_form
from giveaways.models import Giveaway


def giveaways_view(request):
    return render(request, 'giveaway.html', {})


def giveaway_detail(request, id):
    giveaway = Giveaway.objects.filter(id)
    return render(request, 'giveaway_details.html', {'giveaway': giveaway})


def giveaway_add(request):
    form=giveaway_form(request.POST or None , request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Giveaway Details saved")
    return render(request, 'giveaway_add.html', {})


def giveaway_delete(request):
    return render(request, 'giveaway_detail.html', {})
