from datetime import timezone, datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    title = models.CharField(verbose_name="عنوان")
    content = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="images/post", verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان ادیت ")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:post_detail", kwargs={"slug": self.slug})

    from django.utils.html import format_html

    def show_image(self):
        if self.image:
            return format_html('<img src="{}" width="50" height="60" />', self.image.url)
        return "No Image"

    show_image.short_description = "Image"

    def __str__(self):
        return f"{self.title} - {self.content[:30]}"

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="نویسنده")
    body = models.TextField(verbose_name="متن")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="پست")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies",
                               verbose_name="پدر")
    created = models.DateTimeField(auto_now=True, verbose_name="زمان ایجاد")

    def __str__(self):
        return f"{self.author} - {self.body[:30]}"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=100, verbose_name="عنوان")
    message = models.TextField(verbose_name="پیام")

    def __str__(self):
        return f"{self.name} {self.subject}"

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"


class Like(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE , related_name="likes",verbose_name="کاربر")
    post= models.ForeignKey(Post,on_delete=models.CASCADE , related_name="likes",verbose_name="پست ها")
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} {self.post.title}"
    class Meta:
        verbose_name = "لایک"
        verbose_name_plural="لایک ها"