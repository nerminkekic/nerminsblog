from django.db import models

#Model for blog post
class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_date = models.DateTimeField('date published')
    post_body = models.TextField()
    post_author = models.CharField(max_length=250, default='Nermin Kekic')
    slug = models.SlugField(max_length=250, unique=True)
    excerpt = models.TextField()
    
    created_at = models.DateTimeField('date created', auto_now_add=True )
    published_at = models.DateTimeField('date published', null=True, blank=True)
    updated_at = models.DateTimeField('last modified', auto_now=True)
    is_published = models.BooleanField(default=False)
    


    def __str__(self):
        return self.post_title




