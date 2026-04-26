from django.shortcuts import render

from post_app.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    recent_posts = Post.objects.order_by('-updated')[:3]

    return render(request,"home_app/index.html",{"posts":posts,"recent_posts":recent_posts})