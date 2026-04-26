from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView

from post_app.forms import MessageForm
from post_app.models import Post, Category, Comment, Message, Like


# Create your views here.
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(body=body, post=post, author=request.user, parent_id=parent_id)
    recently_post = Post.objects.all().order_by('-updated')[:3]
    if request.user.is_authenticated:
        if request.user.likes.filter(post__slug=slug, user_id=request.user.id).exists():
            is_like = True
        else:
            is_like = False
    else:
        is_like = False
    return render(request, "post_app/post_details.html",
                  {"post": post, "recently_post": recently_post, "is_like": is_like})


def post_list(request):
    posts = Post.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page_number)
    # page_limit
    page_limit = 3
    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 1, 1)
    end_page = min(start_page + page_limit - 1, total_pages)
    if end_page - start_page < page_limit:
        start_page = max(end_page - page_limit + 1, 1)
    page_range = range(start_page, end_page + 1)
    return render(request, "post_app/posts_list.html", {"posts": page_obj, "page_range": page_range})


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    posts = category.post_set.all()
    return render(request, "post_app/posts_list.html", {"posts": posts})


def search(request):
    query = request.GET.get("q")
    posts = Post.objects.filter(title__icontains=query)
    # paginator
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # page_limit
    page_limit = 3
    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 1, 1)
    end_page = min(start_page + page_limit - 1, total_pages)
    if end_page - start_page < page_limit:
        start_page = max(end_page - page_limit + 1, 1)
    page_range = range(start_page, end_page + 1)
    return render(request, "post_app/posts_list.html", {"posts": page_obj, "page_range": page_range})


class MessageFormView(FormView):
    form_class = MessageForm
    template_name = "post_app/contact.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def like_post(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(post__slug=slug, user_id=request.user.id)
            like.delete()
        except:
            like = Like.objects.create(post_id=pk, user_id=request.user.id)
        return redirect("post:post_detail", slug)
    else:
        return redirect("account_app:login")
