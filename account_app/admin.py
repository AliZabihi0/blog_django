from django.contrib import admin
from django.contrib.auth.models import User

from account_app.models import Profile

# Register your models here.
admin.site.register(Profile)

