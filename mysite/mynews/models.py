from django.db import models

# Create your models here.
class Newsarticle(models.Model):

    timestamp=models.TextField(max_length=40)
    news_title = models.TextField(max_length=2000)
    img_source_url=models.TextField(max_length=500)
    author=models.TextField(max_length=20)