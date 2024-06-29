from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # on_delete=models.CASCADE Yazar Silinirse Yazarın Tüm Postları silinir