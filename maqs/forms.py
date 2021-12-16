from django import forms
from .models import Mails


# class ContactForm(forms.ModelForm):
#   # name = forms.CharField(max_length = 30, required = True)
#   # from_email = forms.EmailField(required = True)
#   # subject = forms.CharField(max_length = 50, required = True)
#   # message = forms.CharField(widget = forms.Textarea, required = True)
#
#   class Meta:
#     model = Mails
#     # fields = ('name', 'from_email', 'subject', 'message')
#     fields = '__all__'


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(self):
        return self.from_email
