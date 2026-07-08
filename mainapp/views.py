from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    Event,
    Gallery,
    Song,
    Announcement,
    Member,
)
from .forms import ContactForm


def home(request):

    events = Event.objects.all()
    gallery = Gallery.objects.all()
    music = Song.objects.all()
    announcements = Announcement.objects.order_by("-submitted_at")
    members = Member.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully."
            )
            return redirect("home")

    else:
        form = ContactForm()

    context = {
        "events": events,
        "gallery": gallery,
        "music": music,
        "announcements": announcements,
        "members": members,
        "form": form,
    }

    return render(request, "home.html", context)
