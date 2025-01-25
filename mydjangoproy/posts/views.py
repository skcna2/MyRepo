from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    #agregamos la template
    return render(request, 'posts/posts_list.html', {'posts':posts})
  

