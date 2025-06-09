from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import BookingForm, ContactForm, CustomUserCreationForm, CustomAuthenticationForm


def home_view(request):
    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('home')
        elif 'booking_submit' in request.POST:
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking_form.save()
                return redirect('home')

    contact_form = ContactForm()
    booking_form = BookingForm()
    context = {
        'contact_form': contact_form,
        'booking_form': booking_form,
    }
    return render(request, 'SpaceX.html', context)


def login_register_view(request):
    login_form = CustomAuthenticationForm()
    register_form = CustomUserCreationForm()

    if request.method == 'POST':
        # Obsługa formularza rejestracji
        if 'register_submit' in request.POST:
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, 'Gratulacje! Udało Ci się stworzyć konto.')
                return redirect('main')  # Przekierowujemy na główny hub

        # Obsługa formularza logowania
        elif 'login_submit' in request.POST:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main')

    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')  # Przekierowujemy na główny hub po wylogowaniu

def index_view(request):
    return render(request, 'index.html')


def main_view(request):
    return render(request, 'main.html')


def premium_view(request):
    return render(request, 'premium.html')


def tesla_view(request):
    return render(request, 'tesla.html')


def tesla_kontakt_view(request):
    return render(request, 'tesla-kontakt.html')


def tesla_onas_view(request):
    return render(request, 'tesla-onas.html')