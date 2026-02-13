from post_app.models import Post, Category


def recent_posts(request):
    recent_post = Post.objects.order_by('-updated')[:4]

    return {'recent_post': recent_post }

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories }