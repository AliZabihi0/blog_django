from django.shortcuts import render,get_object_or_404

from post_app.models import Post, Category


# Create your views here.
def post_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    recently_post = Post.objects.all().order_by('-updated')[:3]

    return render(request,"post_app/post_details.html",{"post":post,"recently_post":recently_post})

def post_list(request):
    posts = Post.objects.all()
    return render(request,"post_app/posts_list.html",{"posts":posts})

def category_detail(request, pk):
    category = get_object_or_404(Category,id=pk)
    posts = category.post_set.all()
    return render(request,"post_app/posts_list.html",{"posts":posts})