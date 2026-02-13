from django.urls import path
from django.views.generic import detail
from . import views
app_name = 'post'
urlpatterns = [
    path('detail/<slug:slug>',views.post_detail, name="post_detail"),
    path('list',views.post_list, name="post_list"),
    path('category/<int:pk>',views.category_detail, name="category_detail"),

]
