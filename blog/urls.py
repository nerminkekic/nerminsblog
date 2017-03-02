from django.conf.urls import url
from blog.views import PostListView

app_name = 'blog'

urlpatterns = [
    #blog/
    url(r'^$', PostListView.as_view(), name='blog_index'),
    
]