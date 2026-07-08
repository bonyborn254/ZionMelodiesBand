from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "phone",
            "message"
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "id": "name",
                "placeholder": "Your Name",
                "class": "w-full p-3 rounded-lg bg-white/5 border border-white/10 focus:border-yellow-400 focus:ring-0 outline-none transition text-white placeholder-slate-400"
            }),

            "email": forms.EmailInput(attrs={
                "id": "email",
                "placeholder": "Your Email",
                "class": "w-full p-3 rounded-lg bg-white/5 border border-white/10 focus:border-yellow-400 focus:ring-0 outline-none transition text-white placeholder-slate-400"
            }),

            "phone": forms.TextInput(attrs={
                "id": "phone",
                "placeholder": "Your Phone Number",
                "class": "w-full p-3 rounded-lg bg-white/5 border border-white/10 focus:border-yellow-400 focus:ring-0 outline-none transition text-white placeholder-slate-400"
            }),

            "message": forms.Textarea(attrs={
                "id": "message",
                "rows": 5,
                "placeholder": "Write your message...",
                "class": "w-full p-3 rounded-lg bg-white/5 border border-white/10 focus:border-yellow-400 focus:ring-0 outline-none transition resize-none text-white placeholder-slate-400"
            }),
        }
