from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE) # on_delete=models.CASCADE Yazar Silinirse Yazarın Tüm Postları silinir
    tags = models.ManyToManyField(Tag, blank=True) # blank=True Post oluşturlurken tags alanı boş bırakılabilir demek

    def __str__(self):
        return self.title




