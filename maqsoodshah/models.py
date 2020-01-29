from django.db import models


# Create your models here.
class Mails(models.Model):
  # name = models.CharField(max_length = 30)
  from_email = models.EmailField()
  subject = models.CharField(max_length = 50)
  message = models.CharField(max_length = 1000)

  def __str__(self):
    return self.from_email
