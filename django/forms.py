# plik: core/forms.py

from django import forms
from .models import Booking, ContactMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['created_at']

        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Adres Email',
            'phone': 'Numer telefonu',
            'departure_date': 'Preferowany dzień odlotu',
            'passengers': 'Ilość pasażerów',
            'special_requests': 'Specjalne prośby',
            'terms_agreed': 'Zgadzam się na warunki lotu',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Wpisz swoje imię'}),
            'last_name': forms.TextInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Wpisz swoje nazwisko'}),
            'email': forms.EmailInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Wpisz swój email'}),
            'phone': forms.TextInput(attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                                            'placeholder': 'Wpisz swój numer telefonu'}),
            'departure_date': forms.DateInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded', 'type': 'date'}),
            'passengers': forms.NumberInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Wpisz ilość pasażerów'}),
            'special_requests': forms.Textarea(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded h-32',
                       'placeholder': 'Wpisz swoje prośby'}),
            'terms_agreed': forms.CheckboxInput(
                attrs={'class': 'h-4 w-4 text-primary border-gray-300 rounded focus:ring-primary mr-2'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        exclude = ['created_at']
        labels = {
            'name': 'Twoje imię',
            'email': 'Email',
            'subject': 'Wpisz swoją sprawę',
            'message': 'Twoja wiadomość',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                                           'placeholder': 'Wpisz swoje imię'}),
            'email': forms.EmailInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Wpisz swój email'}),
            'subject': forms.TextInput(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded',
                       'placeholder': 'Temat'}),
            'message': forms.Textarea(
                attrs={'class': 'w-full bg-gray-800 border border-gray-700 text-white p-3 rounded h-40',
                       'placeholder': 'Wpisz swoją wiadomość'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Login"
        self.fields['password1'].label = "Hasło"
        self.fields['password2'].label = "Potwierdź hasło"