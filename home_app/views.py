from django.shortcuts import render

from post_app.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()


    return render(request,"home_app/index.html",{"posts":posts,})