from django import forms

from post_app.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control","placeholder":" Your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder":" Your email"}),
            "subject": forms.TextInput(attrs={"class": "form-control","placeholder":" Your subject"}),
            "message" : forms.Textarea(attrs={"class": "form-control","placeholder":" Your message"})
        }
