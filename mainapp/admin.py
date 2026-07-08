from django.contrib import admin
from .models import (
    Event,
    Gallery,
    Song,
    Announcement,
    Member,
    ContactMessage,
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "description")


@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "leader",
        "music_key",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "title",
        "leader",
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "submitted_at",
    )
    ordering = ("-submitted_at",)
    search_fields = ("title",)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "section",
    )
    search_fields = (
        "name",
        "role",
        "section",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "submitted_at",
    )
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at",)
    search_fields = (
        "name",
        "email",
        "phone",
    )
