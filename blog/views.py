from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    me = User.objects.get(username='tanya95')
    Post.objects.create(author=me, title='Sample title2', text='Test2')
    Post.objects.create(author=me, title='Sample title3', text='Test3')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})