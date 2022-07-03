from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  phone = models.CharField(max_length=11, null=True, blank=True)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  complete = models.BooleanField(default=False )
  def __str__(self):
    return self.phone


class History(models.Model):
  history = models.CharField(max_length=100, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  