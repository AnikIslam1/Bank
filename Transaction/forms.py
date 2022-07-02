from django import forms

class Payment(forms.Form):
  Sender_Phone = forms.CharField(max_length=11)
  Receiver_Phone = forms.CharField(max_length=11)
  amount = forms.CharField(max_length=30)