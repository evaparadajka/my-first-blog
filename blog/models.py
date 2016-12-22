from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Klient(models.Model):
    author = models.ForeignKey('auth.User')
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    numerkarty = models.CharField(max_length=200)
    uwagi = models.CharField(max_length=200)
    styl = models.CharField(max_length=200)
    instruktor = models.CharField(max_length=200)
    poziom = models.CharField(max_length=200)
    imie = models.CharField(max_length=200)
    dzien = models.CharField(max_length=200)
    wazneod = models.DateTimeField(blank=True, null=True)
    waznedo = models.DateTimeField(blank=True, null=True)
    ilosc = models.CharField(max_length=200)
    pozostalo = models.CharField(max_length=200)


    def publish(self):
        self.save()

    def __str__(self):
        return self.numerkarty
