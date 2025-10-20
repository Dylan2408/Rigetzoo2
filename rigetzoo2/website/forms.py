from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import PasswordInput, TextInput, EmailInput

# Register
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    email = forms.CharField(widget=EmailInput())

class Zoo_Booking_Form(forms.ModelForm):

    class Meta:
        model = ZooBooking

        fields = ['zoo_booking_date_arrive', 'zoo_booking_adults', 'zoo_booking_children','zoo_booking_oap', 'zoo_booking_cost']

        lables = {
            "hotel_booking_date_arrive": 'day you wish to arrive?',
        }

        widgets = {
            'hotel_booking_date_arrrive': forms.DateInput(attrs={'type': 'date'}),
            'hotel_total_cost': forms.HiddenInput(),
        }

    def __init__(self, *args **kwargs):
        super{}.__init__{*args**kwargs}