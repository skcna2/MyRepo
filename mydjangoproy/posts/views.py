from django.shortcuts import render

# Create your views here.
def post_list(request):
    #agregamos la template
    return render(request, 'post_list.html')  