from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class IndexPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('index'))

    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_tempates_base(self):
        self.assertTemplateUsed(self.response, 'base.html')

    def test_tempates_message(self):
        self.assertTemplateUsed(self.response, 'messages.html')


class SignUpTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('sign_up'))

    def test_sign_up_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_simple_post_1(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('username', response.context)

    def test_simple_post_2(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('first_name', response.context)

    def test_simple_post_3(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('last_name', response.context)

    def test_simple_post_4(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('email', response.context)

    def test_simple_post_5(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('password', response.context)

    def test_simple_post_6(self):
        response = self.client.post(reverse('sign_up'),
                                    {'username': 'mary', 'first_name': 'Зудилина', 'last_name': 'Мария',
                                     'email': '1@mail.ru', 'password': 1616, 'status': 'STU'})
        self.assertIsNotNone('status', response.context)

    def test_tempates(self):
        self.assertTemplateUsed(self.response, 'messages.html')


class SignInTestCase(TestCase):
    fixtures = ['test_database.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.get(username='bear_16')
        self.client.force_login(user=self.user)
        self.response = self.client.get(reverse('sign_in'))

    def test_sign_in_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response(self):
        c = Client()
        response = c.post('/sign_in', {'username': 'bear_16', 'password': '1616'})
        self.assertEqual(302, response.status_code)

    def test_redirect(self):
        c = Client()
        response = c.post('/sign_in', {'username': 'bear_16', 'password': '1616'})
        self.assertRedirects(response, reverse('index'))

    def test_simple_post(self):
        response = self.client.post(reverse('sign_in'), {'username': 'bear_16', 'password': 1616})
        self.assertIsNotNone('username', response.context)

    def test_tempates(self):
        self.assertTemplateUsed(self.response, 'messages.html')


class LogOutPageTestCase(TestCase):
    fixtures = ['test_database.json']

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.get(username='bear_16')
        self.client.force_login(user=self.user)
        self.response = self.client.get(reverse('log_out'))

    def test_log_out_response(self):
        client = Client()
        response = client.get(reverse('log_out'), follow=False)
        self.assertEqual(302, response.status_code)

    def test_redirect(self):
        client = Client()
        response = client.get(reverse('log_out'), follow=True)
        self.assertRedirects(response, '/', status_code=302)

    def test_response(self):
        self.assertEqual(302, self.response.status_code)


class SectionsPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get(reverse('sections'))

    def test_sections_response(self):
        self.assertEqual(self.response.status_code, 200)


class BySectionsPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get('/section/1')

    def test_by_section_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_tempates(self):
        self.assertTemplateUsed(self.response, 'messages.html')


class BySectionPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get('/section/2')

    def test_by_section_response(self):
        self.assertEqual(self.response.status_code, 200)


class ByPostPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get('/post/1')

    def test_by_post_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_tempates(self):
        self.assertTemplateUsed(self.response, 'messages.html')


class ByPostsPageTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.response = self.client.get('/post/2')

    def test_by_post_response(self):
        self.assertEqual(self.response.status_code, 200)


class ChangePasswordPageTestCase(TestCase):
    fixtures = ['test_database.json']

    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.get(username='bear_16')
        self.client.force_login(user=self.user)
        self.response = self.client.get(reverse('change_password'))

    def test_change_password_response(self):
        self.assertEqual(200, self.response.status_code)

    def test_response_true(self):
        response = self.client.get(reverse('change_password'), follow=True)
        self.assertEqual(200, response.status_code)

    def test_simple_post_1(self):
        response = self.client.post(reverse('change_password'), {'old_password': 1616, 'new_password': 1616})
        self.assertIsNotNone('old_password', response.context)

    def test_simple_post_2(self):
        response = self.client.post(reverse('change_password'), {'old_password': 1616, 'new_password': 1616})
        self.assertIsNotNone('new_password', response.context)
