from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import customer
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
      x = form.cleaned_data['Sender_Name']
      y = form.cleaned_data['Receiver_Name']
      z = decimal.Decimal(form.cleaned_data['amount'])

      Sender_Name = customer.objects.select_for_update().get(name=x)
      Receiver_Name = customer.objects.select_for_update().get(name=y)

    with transaction.atomic():
      Sender_Name.balance -= z
      Sender_Name.last_transection = z
      Sender_Name.save()

      Receiver_Name.balance += z
      Receiver_Name.last_transection = z
      Receiver_Name.save()

      #customer.objects.filter(name=x).update(balance=F('balance') - z)
      #customer.objects.filter(name=y).update(balance=F('balance') + z)

      return HttpResponseRedirect('/')

  else:
    form = Payment()

  return render(request, 'index.html', {'form': form})

#Rest API
class User(generics.ListCreateAPIView):
  queryset = customer.objects.all()
  serializer_class = CustomerSerializer


class Customer_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = CustomerSerializer

