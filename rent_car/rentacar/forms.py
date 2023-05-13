from django import forms
from rentacar.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'start_date', 'end_date', 'customer_name', 'phone', 'email', 'text']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=300)
    email = forms.EmailField()
    contant = forms.CharField(widget=forms.Textarea)

