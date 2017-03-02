from django.db import models

#Model for blog post
class Post(models.Model):
    post_title = models.CharField(max_length=250)
    post_date = models.DateTimeField('date published')
    post_body = models.TextField()
    post_author = models.CharField(max_length=250, default='Nermin Kekic')

    def __str__(self):
        return self.post_title




