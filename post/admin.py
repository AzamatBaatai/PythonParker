from django.contrib import admin

# Register your models here.


# Zdes registriruetsya modeli dlya ih otobrajeniya admin-paneli
from post.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
