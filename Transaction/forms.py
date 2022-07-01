from django import forms

class Payment(forms.Form):
  Sender_Name = forms.CharField(max_length=30)
  Receiver_Name = forms.CharField(max_length=30)
  amount = forms.CharField(max_length=30)