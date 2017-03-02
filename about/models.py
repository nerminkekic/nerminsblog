from django.db import models

# This is the model for about page
class About(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

    




