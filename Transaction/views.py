from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import account
from .models import History
from django.db.models import F
import decimal
from django.db import transaction
from rest_framework import generics
from .serializers import UserSerializer
from .serializers import HistorySerializer
import schedule
import time



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
    
      h = "Phone {} send {}TK amount to Phone {}".format(x,z,y)
      History.objects.create(history=h)
      Sender_Phone.balance -= z
      Sender_Phone.save()
      
      Receiver_Phone.balance += z
      Receiver_Phone.save()

      
      #customer.objects.filter(name=x).update(balance=F('balance') - z)
      #customer.objects.filter(name=y).update(balance=F('balance') + z)

      return HttpResponseRedirect('/')
  elif request.method == 'PUT':
    #Time
    t = form.cleaned_data['']
    schedule.every().day.at("10:30").do(request)
    while True:
      schedule.run_pending()
      time.sleep(1)
  else:
    form = Payment()

  return render(request, 'index.html', {'form': form})

    


#Rest API
class Account_User(generics.ListCreateAPIView):
  queryset = account.objects.all()
  serializer_class = UserSerializer


class Account_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = account.objects.all()
    serializer_class = UserSerializer

class History_User(generics.ListCreateAPIView):
  queryset = History.objects.all()
  serializer_class = HistorySerializer

class History_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

