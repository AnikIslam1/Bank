from django.db import models


# Create your models here.
class customer(models.Model):
  name = models.CharField(max_length=50)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  transaction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  def __str__(self):
    return self.name