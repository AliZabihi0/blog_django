from django.urls import path
from django.views.generic import detail
from . import views

app_name = 'post'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name="post_detail"),
    path('list', views.post_list, name="post_list"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search, name="search_list"),
    path('contact', views.MessageFormView.as_view(), name="contact_form"),
    path('like/<slug:slug>/<int:pk>', views.like_post, name="like"),

]
