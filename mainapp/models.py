from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
