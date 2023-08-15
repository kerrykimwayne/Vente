from django.shortcuts import render,get_object_or_404
from .models import pagne,categorie

# Create your views here.
def acceuil(request):
    pagnes=pagne.objects.all()[:9]
    catego=categorie.objects.all()
    return render(request,'pagne/index.html',context={'pagnes':pagnes,'categorie':catego})


def contact(request):
    return render(request,'pagne/contact.html')


def prod_anc(request):
    ancien=pagne.objects.all()
    return render(request,'pagne/produit_ancienne.html',context={'ancien':ancien})

def detail_produit(request,slug):
    detail_prod=get_object_or_404(pagne,slug=slug)
    return render(request,'pagne/detail_produit.html',context={'detail_prod':detail_prod})

def filter(request,slug):
    catego=categorie.objects.all()
    filtres=get_object_or_404(categorie,slug=slug)
    if slug == 'All':
        prod=pagne.objects.all()
    if slug == 'WAX':
        prod=pagne.objects.all().filter(Libele='CELEBRITY WAX')
    if slug == 'TOP_HOLLANDAIS':
        prod=pagne.objects.all().filter(Libele='TOP HOLLANDAIS')
    if slug == 'MAJESTIC':
        prod=pagne.objects.all().filter(Libele='MAJESTIC')
    if slug == 'Nouveau':
        prod=pagne.objects.all()[:9]
    return render(request,'pagne/filtre.html',context={'filtres':filtres,'produit':prod,'categorie':catego})