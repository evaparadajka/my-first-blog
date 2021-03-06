from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Klient
from .models import Zliczenie
from .models import Filtr
from .models import Wplata
from .forms import PostForm
from .forms import KlientForm
from .forms import ZnajdzForm
from .forms import FiltrujForm
from .forms import WplataForm
from django.shortcuts import redirect
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = posts.reverse()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def klient_list(request):
    klients = Klient.objects.order_by('numerkarty')
    return render(request, 'blog/klient_list.html', {'klients': klients})
def zarzadzaj(request):
    return render(request, 'blog/zarzadzaj.html')
def klient_detail(request, numerkarty):
    klient = get_object_or_404(Klient, numerkarty=numerkarty)
    return render(request, 'blog/klient_detail.html', {'klient': klient})
def klient_new(request):
    if request.method == "POST":
        form = KlientForm(request.POST)
        if form.is_valid():
            klient = form.save(commit=False)
            klient.author = request.user
            klient.save()
            return redirect('klient_detail', numerkarty=klient.numerkarty)
    else:
        form = KlientForm()
    return render(request, 'blog/klient_edit.html', {'form': form})
def klient_edit(request, numerkarty):
    klient = get_object_or_404(Klient, numerkarty=numerkarty)
    if request.method == "POST":
        form = KlientForm(request.POST, instance=klient)
        if form.is_valid():
            klient = form.save(commit=False)
            klient.author = request.user
            klient.save()
            return redirect('klient_detail', numerkarty=numerkarty)
    else:
        form = KlientForm(instance=klient)
    return render(request, 'blog/klient_edit.html', {'form': form})
def klient_odlicz(request, numerkarty):
    klient = get_object_or_404(Klient, numerkarty=numerkarty)
    klient.pozostalo = klient.pozostalo - 1
    odliczenie = str(timezone.now())
    odliczenie = odliczenie[0:10]
    klient.uczestniczyl = klient.uczestniczyl + " " + odliczenie
    klient.save()
    return redirect('klient_detail', numerkarty=klient.numerkarty)
def odlicz_zajecia(request):
    if request.method == "POST":
        form = ZnajdzForm(request.POST)
        if form.is_valid():
            zliczenie = form.save(commit=False)
            doodliczenia = zliczenie.numerkarty
            klient = get_object_or_404(Klient, numerkarty=zliczenie.numerkarty)
            return redirect('klient_detail', numerkarty=klient.numerkarty)
    else:
        form = ZnajdzForm()
    return render(request, 'blog/odlicz_zajecia.html', {'form': form})
def filtruj(request):
    if request.method == "POST":
        form = FiltrujForm(request.POST)
        if form.is_valid():
            filtr = form.save(commit=False)
            klients = Klient.objects.filter(styl__contains = filtr.styl) & Klient.objects.filter(instruktor__contains = filtr.instruktor) & Klient.objects.filter(poziom__contains = filtr.poziom) & Klient.objects.filter(dzien__contains = filtr.dzien)
            return render(request, 'blog/filtruj.html', {'klients': klients})
    else:
        form = FiltrujForm()
    return render(request, 'blog/filtruj.html', {'form': form})
def wplaty(request):
    wplatas = Wplata.objects.order_by('data_wplaty')
    wplatas = wplatas.reverse()
    return render(request, 'blog/wplaty.html', {'wplatas': wplatas})
def nowa_wplata(request):
    if request.method == "POST":
        form = WplataForm(request.POST)
        if form.is_valid():
            wplata = form.save(commit=False)
            wplata.save()
            return redirect('wplaty')
    else:
        form = WplataForm()
    return render(request, 'blog/nowa_wplata.html', {'form': form})
def automatycznie_odlicz_zajecia(request):
    if request.method == "POST":
        form = ZnajdzForm(request.POST)
        if form.is_valid():
            zliczenie = form.save(commit=False)
            doodliczenia = zliczenie.numerkarty
            klient = get_object_or_404(Klient, numerkarty=zliczenie.numerkarty)
            return redirect('automatycznie_klient_odlicz', numerkarty=klient.numerkarty)
    else:
        form = ZnajdzForm()
    return render(request, 'blog/automatycznie_odlicz_zajecia.html', {'form': form})
def automatycznie_klient_odlicz(request, numerkarty):
    klient = get_object_or_404(Klient, numerkarty=numerkarty)
    waznosc = str(klient.waznedo)
    odliczenie = str(timezone.now())
    odliczenie = odliczenie[0:10]
    if klient.pozostalo>0:
        if waznosc>odliczenie:
            klient.pozostalo = klient.pozostalo - 1
            klient.uczestniczyl = klient.uczestniczyl + " " + odliczenie
            klient.save()
            return redirect('zezwolenie')
    return redirect('brak_zezwolenia', numerkarty=klient.numerkarty)
def zezwolenie(request):
    return render(request, 'blog/zezwolenie.html')
def brak_zezwolenia(request, numerkarty):
    klient = get_object_or_404(Klient, numerkarty=numerkarty)
    return render(request, 'blog/brak_zezwolenia.html', {'klient': klient})
