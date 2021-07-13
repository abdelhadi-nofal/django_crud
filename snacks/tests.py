from django.http import response
from django.test import TestCase
from .models import Snack
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class SnackTests(TestCase):
    def test_snack_list_status_code(self):
        url = reverse('snack')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code,expected_status_code)



    def test_snack_list_template(self):
            url = reverse('snack')
            response = self.client.get(url)
            actual = 'snack.html'
            self.assertTemplateUsed(response, actual)

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'emailtest',
            password = '123456',
        )

        self.snack = Snack.objects.create(
            title = 'Testing Snack',
            purchaser = self.user,
            description = 'Testing description',
        )



    def test_snack_create(self):
        response = self.client.post(
            reverse('snackcreate'),
            {'title' : 'Testing title','purchaser' : self.user ,'description' : 'Testing description'}
            )

        get_response = self.client.get(reverse('snack'))

        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Testing t')
        self.assertEqual(200,get_response.status_code)