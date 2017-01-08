from django import forms
from .models import Post
from .models import Klient
from .models import Zliczenie
from .models import Filtr
from .models import Wplata

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ('imie', 'nazwisko', 'telefon', 'email', 'numerkarty', 'uwagi', 'styl', 'instruktor', 'poziom', 'dzien', 'wazneod', 'waznedo', 'uczestniczyl', 'ilosc', 'pozostalo',)

class ZnajdzForm(forms.ModelForm):
    class Meta:
        model = Zliczenie
        fields = ('numerkarty',)

class FiltrujForm(forms.ModelForm):
    styl = forms.CharField(required=False)
    instruktor = forms.CharField(required=False)
    poziom = forms.CharField(required=False)
    dzien = forms.CharField(required=False)
    class Meta:
        model = Klient
        fields = ('styl', 'instruktor', 'poziom', 'dzien',)

class WplataForm(forms.ModelForm):
    class Meta:
        model = Wplata
        fields = ('imie', 'nazwisko', 'data_wplaty', 'kwota',)
