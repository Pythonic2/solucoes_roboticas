from django.db import models

# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email_addres = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)
    message = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.full_name
