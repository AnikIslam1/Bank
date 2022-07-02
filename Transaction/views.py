from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import account
from django.db.models import F
import decimal
from django.db import transaction
from rest_framework import generics
from .serializers import CustomerSerializer


#transection function
def process_payment(request):

  if request.method == 'POST':

    form = Payment(request.POST)

    if form.is_valid():
      x = form.cleaned_data['Sender_Phone']
      y = form.cleaned_data['Receiver_Phone']
      z = decimal.Decimal(form.cleaned_data['amount'])

      Sender_Phone = account.objects.select_for_update().get(phone=x)
      Receiver_Phone = account.objects.select_for_update().get(phone=y)

    with transaction.atomic():
      Sender_Phone.balance -= z
      Sender_Phone.save()

      Receiver_Phone.balance += z
      Receiver_Phone.save()

      #customer.objects.filter(name=x).update(balance=F('balance') - z)
      #customer.objects.filter(name=y).update(balance=F('balance') + z)

      return HttpResponseRedirect('/')

  else:
    form = Payment()

  return render(request, 'index.html', {'form': form})

#Rest API
class Account(generics.ListCreateAPIView):
  queryset = account.objects.all()
  serializer_class = CustomerSerializer


class Account_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = account.objects.all()
    serializer_class = CustomerSerializer

