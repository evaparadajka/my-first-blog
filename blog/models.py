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
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)
    telefon = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    numerkarty = models.CharField(max_length=20)
    uwagi = models.CharField(max_length=50)
    styl = models.CharField(max_length=20)
    instruktor = models.CharField(max_length=70)
    poziom = models.CharField(max_length=20)
    dzien = models.CharField(max_length=20)
    wazneod = models.DateField(blank=True, null=True)
    waznedo = models.DateField(blank=True, null=True)
    uczestniczyl = models.TextField()
    ilosc = models.IntegerField()
    pozostalo = models.IntegerField()


    def publish(self):
        self.save()

    def __str__(self):
        return self.numerkarty

class Zliczenie(models.Model):
    numerkarty = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.numerkarty

class Filtr(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)
    styl = models.CharField(max_length=20)
    instruktor = models.CharField(max_length=70)
    poziom = models.CharField(max_length=20)
    dzien = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.atrybut

class Wplata(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=40)
    data_wplaty = models.DateField(blank=True, null=True)
    kwota = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.kwota
