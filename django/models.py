
from django.db import models

# Model dla rezerwacji lotu na Marsa
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    departure_date = models.DateField()
    passengers = models.IntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    terms_agreed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rezerwacja: {self.first_name} {self.last_name} - {self.departure_date}"

# Model dla wiadomości z formularza kontaktowego
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wiadomość od: {self.name} - {self.subject}"