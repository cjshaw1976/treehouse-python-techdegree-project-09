from django import forms

from django.utils import timezone

from .models import Menu, Item


def now_plus_one_year():
    return timezone.now() + timezone.timedelta(days=365)


class MenuForm(forms.ModelForm):
    items = (forms.ModelMultipleChoiceField(queryset=Item.objects.all(),
             widget=forms.SelectMultiple()))
    expiration_date = forms.DateField(input_formats=['%Y-%m-%d',
                                                     '%m/%d/%Y',
                                                     '%m/%d/%y'],
                                      widget=forms.SelectDateWidget(),
                                      initial=now_plus_one_year())

    class Meta:
        model = Menu
        exclude = ('created_date',)
