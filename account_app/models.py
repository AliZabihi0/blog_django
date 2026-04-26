from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="کاربر")
    bio = models.TextField(max_length=500, blank=True,verbose_name="بایو")
    image = models.ImageField(upload_to='profile_pics', blank=True,verbose_name="تصویر")

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name= "حساب کاربری"
        verbose_name_plural="حساب های کاربری"

