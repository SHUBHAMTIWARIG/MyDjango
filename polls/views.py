from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# from polls.forms import DocumentForm, creator_form
# from polls.models import post, Document, creator


@login_required
def home(request):
    # posts = post.objects.all()
    return render(request, 'base.html', {})
