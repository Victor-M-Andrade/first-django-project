from django.shortcuts import render, get_list_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    #com filtro
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #sem filtro
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})