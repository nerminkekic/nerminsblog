from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

#Register Post model to admin site 
#admin.site.register(Post)

class PostAdmin(SummernoteModelAdmin):
    model = Post
    
admin.site.register(Post, PostAdmin)


