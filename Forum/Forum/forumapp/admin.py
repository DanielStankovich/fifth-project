from django.contrib import admin

from . import models

from .models import Category
from .models import Post
from .models import Profile
# Register your models here.
admin.site.register(models.Post)

admin.site.register(models.Category)

admin.site.register(Profile)
