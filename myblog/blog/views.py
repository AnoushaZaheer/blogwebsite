from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from core.models import *
from core.forms import ContactForm

# Create your views here.
def home(request):

    posts = post.objects.filter(status=post.ACTIVE).annotate(num_comments=Count('commentr'))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # form = ContactForm()

            return render(request, 'blog/home.html', {'posts':posts,'form': ContactForm(), 'thank_you': True})
    else:
        form = ContactForm()
    return render(request, 'blog/home.html', {'posts':posts,'form': form})



def about(request):
    return render(request, 'blog/about.html')

