from django.shortcuts import render, get_object_or_404, redirect
from .models import post, comments,Category
from .forms import commentform
from django.db.models import Q
from django.http.response import HttpResponse
from django.http import HttpResponse

def details(request, category_slug, slug, status=post.ACTIVE):
    post_instance = get_object_or_404(post, slug=slug) 
    comments_list = comments.objects.filter(post_f=post_instance)
    
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_f = post_instance
            comment.save()
            return redirect('details', category_slug=category_slug,slug=slug)
    else:
        form = commentform()
    
    return render(request, 'core/details.html', {'post': post_instance, 'comments': comments_list, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=post.ACTIVE)

    return render(request, 'core/category.html', {'category': category, 'posts': posts})



def search(request):
    query = request.GET.get('query', '')

    posts = post.objects.filter(status=post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query': query})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")