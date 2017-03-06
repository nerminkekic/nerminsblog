from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .models import Post

#Register Post model to admin site 
#admin.site.register(Post)
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'is_published',
            'post_title',
            'slug',
            'excerpt',
            'post_body',
        ]
        
        labels = {
            'is_published': 'Is Published?',
        }
    

class PostAdmin(SummernoteModelAdmin):
    model = Post

    form = PostAdminForm

    prepopulated_fields = {
        'slug': ('post_title',)
    }

    def save_model(self, request, obj, form, change):
        if form.has_changed() and 'is_published' in form.changed_data:
            if obj.is_published:
                obj.published_at = now()
            else:
                obj.published_at = None
        
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)


