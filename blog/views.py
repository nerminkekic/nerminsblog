from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from .models import Post

#Display 15 latest blog posts on index page.
class PostListView(ListView):
    template_name = "blog/list.html"

    def get_queryset(self):
        return Post.objects.order_by('-post_date')[:15]



