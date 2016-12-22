from django import forms
from .models import Post
from .models import Klient

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ('imie', 'nazwisko', 'telefon', 'email', 'numerkarty', 'uwagi', 'styl', 'instruktor', 'poziom', 'dzien', 'wazneod', 'waznedo', 'ilosc', 'pozostalo',)
