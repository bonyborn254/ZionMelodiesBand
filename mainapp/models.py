from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# File size validator - 100MB limit
def validate_file_size(file):
    file_size = file.size
    limit_mb = 100
    limit_bytes = limit_mb * 1024 * 1024
    
    if file_size > limit_bytes:
        raise ValidationError(f"File size cannot exceed {limit_mb}MB. Current size: {file_size / (1024 * 1024):.2f}MB")

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", blank=True, null=True, validators=[validate_file_size])

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True, validators=[validate_file_size])
    media_file = models.FileField(upload_to="gallery/media/", blank=True, null=True, validators=[validate_file_size], help_text="Upload video, audio, or other media files (Max: 100MB)")
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
        
class Song(models.Model):
    WORSHIP = "Worship"
    PRAISE = "Praise"

    TYPES = [
        (WORSHIP, "Worship"),
        (PRAISE, "Praise"),
    ]

    title = models.CharField(max_length=200)
    leader = models.CharField(max_length=100)
    music_key = models.CharField(max_length=50)
    category = models.CharField(
        max_length=20,
        choices=TYPES,
        default=WORSHIP
    )

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    messages = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

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
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
