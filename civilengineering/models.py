from django.db import models
from cloudinary.models import CloudinaryField


class Usermodel(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name





class Projectmodel(models.Model):

    CATEGORY = (

        ('trailer','Trailer'),
        ('bts','Behind Scenes'),
        ('interview','Interview'),

    )

    title = models.CharField(max_length=200)

    # YouTube video ID
    video = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="YouTube Video ID"
    )

    # Your uploaded file
    
    

    uploaded_video = CloudinaryField(
        resource_type='video',
        blank=True,
        null=True
    )








    category = models.CharField(
        max_length=20,
        choices=CATEGORY,
        default='trailer'
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    name = models.CharField(max_length=100)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name