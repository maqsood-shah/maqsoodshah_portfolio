from django.http import HttpResponse, Http404, BadHeaderError, HttpResponseRedirect
from django.shortcuts import render, redirect

from portfolio import settings
from . import forms
from .forms import ContactForm
from .models import Mails
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
import time


# from portfolio.settings import EMAIL_HOST_USER


def index(request):
  return render(request, 'index.html')


def download(request):
  with open('maqsoodshah/static/media/MAQSOOD_SHAH_CV.pdf', 'rb') as pdf:
    response = HttpResponse(pdf.read(), content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment;filename=MAQSOOD_SHAH_CV.pdf'
    return response


def email(request):
  sub = forms.ContactForm()
  if request.method == 'GET':
    form = ContactForm()
    messages.success(request, 'Please fill the form.')
    return render(request, "index.html")
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      from_email = request.POST.get('from_email')
      to_email = 'mr.maqsood.shah@gmail.com'
      time.sleep(2)
      send_mail(subject,
                message, from_email, [to_email], fail_silently = False)
      time.sleep(3)
      data = {
        'subject': subject,
        'message': message,
        'from_email': from_email,
        'to_email': to_email,
      }
      messages.success(request, 'Thank you for contacting me. I will reply soon.')
      return render(request, "email.html", { 'data': data })
    messages.warning(request, "data not valid.")
  return render(request, "index.html")
