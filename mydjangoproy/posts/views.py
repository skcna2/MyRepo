from django.shortcuts import render

# Create your views here.
def posts_list(request):
    #agregamos la template
    return render(request, 'posts/posts_list.html')  