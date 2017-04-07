from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import datetime

from .forms import MenuForm
from .models import Menu, Item


def menu_list(request):
    menus = (Menu.objects.filter(expiration_date__date__gte=datetime.now())
             .order_by('expiration_date').prefetch_related('items'))
    return render(request, 'menu/list_all_current_menus.html',
                  {'menus': menus})


def menu_detail(request, pk):
    menu = Menu.objects.prefetch_related('items').get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'menu/detail_item.html', {'item': item})


# @login_required
def create_new_menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            menu.items = form.cleaned_data['items']
            return redirect('menu_detail', pk=menu.pk)

    return render(request, 'menu/menu_edit.html', {'form': form})


# @login_required
def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    form = MenuForm(instance=menu)
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu.season = form.cleaned_data['season']
            menu.expiration_date = form.cleaned_data['expiration_date']
            menu.items = form.cleaned_data['items']
            menu.save()
            return redirect('menu_detail', pk=menu.pk)

    return render(request, 'menu/menu_edit.html', {'form': form})
