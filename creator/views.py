from django.shortcuts import render
from creator.forms import creator_form
from django.http import HttpResponseRedirect
# Create your views here.
from creator.models import creator


def creator_view(request):
    if request.method == 'POST':
        form = creator_form(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/home')
    else:
        form = creator_form()

    return render(request, "creator.html", {'form': form})


def creator_detail(request):
    return render(request, "creator.html", {})


def creator_add(request):
    return render(request, "creator.html", {})
