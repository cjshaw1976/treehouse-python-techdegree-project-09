from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Menu, Item, Ingredient
from .forms import MenuForm


class MenuViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username='mmmmbop')
        self.user.set_password('whooooo')
        self.user.save()

        # Login test user

        # Create some test ingrediants
        ing1 = Ingredient.objects.create(name='Gin')
        ing2 = Ingredient.objects.create(name='Tonic')
        ing3 = Ingredient.objects.create(name='Lemon')
        ing4 = Ingredient.objects.create(name='Ice')

        # Create a test menu Item
        myitem = Item.objects.create(name='Gin n Tonic',
                                     description='Refreshing on a hot summers day',
                                     chef=self.user)
        self.itemid = myitem.id
        myitem.ingredients.add(ing1, ing2, ing3, ing4)

        # Create a test Menu
        mymenu = Menu.objects.create(season='summer')
        self.menuid = mymenu.id
        mymenu.items.add(myitem)

    def tearDown(self):
        # Remove the test user
        self.user.delete()

    def test_relations(self):
        mydrink = Item.objects.get(name='Gin n Tonic')
        self.assertEqual(self.user, mydrink.chef)

    def test_view_menu_list(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertContains(resp, "summer")

    def test_view_menu_detail(self):
        resp = self.client.get(reverse('menu_detail',
                                       kwargs={'pk': self.menuid}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        self.assertContains(resp, "summer")

    def test_view_item_detail(self):
        resp = self.client.get(reverse('item_detail',
                                       kwargs={'pk': self.itemid}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/detail_item.html')
        self.assertContains(resp, "Gin n Tonic")

    def test_view_menu_new(self):
        resp = self.client.get(reverse('menu_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')

    def test_view_edit_menu(self):
        resp = self.client.get(reverse('menu_edit',
                                       kwargs={'pk': self.menuid}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')
        self.assertContains(resp, "summer")

    def test_form_menuform(self):
        form = MenuForm(data={'season': "winter",
                              'expiration_date': "2017-12-31"})
        self.assertFalse(form.is_valid())
