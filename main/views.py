from django.shortcuts import render

from .models import Index, Right, About, Rightab, Contacts, Rightcon, Menu, Rightmen



def index(request):
    form = Index.objects.order_by('-id')
    right = Right.objects.order_by('-id')

    context = {
        'title': 'CocoTea-Главная',
        'form': form,
        'right': right
    }
    return render(request, 'main/index.html', context)


def about(request):
    formab = About.objects.order_by('-id')
    rightab = Rightab.objects.order_by('-id')

    context = {
        'title': 'CocoTea-Про нас',
        'formab': formab,
        'rightab': rightab
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    formcon = Contacts.objects.order_by('-id')
    rightcon = Rightcon.objects.order_by('-id')

    context = {
        'title': 'CocoTea-Контакты',
        'formcon': formcon,
        'rightcon': rightcon
    }
    return render(request, 'main/contacts.html', context)


def menu(request):
    formmen = Menu.objects.order_by('-id')
    rightmen = Rightmen.objects.order_by('-id')

    context = {
        'title': 'CocoTea-Меню',
        'formmen': formmen,
        'rightmen': rightmen
    }
    return render(request, 'main/menu.html', context)

