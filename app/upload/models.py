## models.py
from djongo import models

# from django.conf import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage


# Define your GrifFSStorage instance 
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join(['myfiles/']))

class IdToken(models.Model):
    token = models.JSONField()
    def __str__(self):
        return self.token

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='persons', storage=grid_fs_storage)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateField()
    person = models.ManyToManyField(Person)

    def __str__(self):
        return self.comment

class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    person = models.ManyToManyField(Person)
    n_likes = models.IntegerField()
    comment =  models.ManyToManyField(Comment)
    rating = models.IntegerField()
    featured_image = models.ImageField(upload_to='entries', storage=grid_fs_storage)

    def __str__(self):
        return self.headline