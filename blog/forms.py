from django import forms
from .models import Post
from .models import Klient
from .models import Zliczenie

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
