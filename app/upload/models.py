## models.py
from djongo import models
# from django.db import models
# from django.conf import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage


# Define your GrifFSStorage instance 
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join(['myfiles/']))

class ObjectIdField(models.Field):
    def __init__(self, *args, **kwargs):
        return self

class IdToken(models.Model):
    # token_id = models.AutoField(primary_key=True)
    _id = models.ObjectIdField()
    token = models.CharField(max_length=200) #models.JSONField()
    
    class Meta:
        indexes = [ ]
    # objects = models.DjongoManager()
   

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='persons', storage=grid_fs_storage)

    class Meta:
        abstract = True


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateField()
    # person = models.Field(Person)
    # person = models.EmbeddedField(
    #     model_container=Person,
    # )
    
    class Meta:
        abstract = True


class Entry(models.Model):
    # entry_id = models.AutoField(primary_key=True)
    _id = models.ObjectIdField()
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()

    # person = models.EmbeddedField(
    #     model_container=Person,
    # )
    # person = models.Field(Person)
    n_likes = models.IntegerField()
    # comment =  models.Field(Comment)
    # comment = models.EmbeddedField(
    #     model_container=Comment,
    # )
    rating = models.IntegerField()
    featured_image = models.ImageField(upload_to='entries', storage=grid_fs_storage, blank=True)

    