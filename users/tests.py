from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "ikromjon",
                "first_name": "Ikromjon",
                "last_name": "Ergashev",
                "email": "ikromjon2@gmail.com",
                "password": "somepassword"
            }
        )

        user = CustomUser.objects.get(username="ikromjon")

        self.assertEqual(user.first_name, "Ikromjon")
        self.assertEqual(user.last_name, "Ergashev")
        self.assertEqual(user.email, "ikromjon2@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Ikromjon",
                "email": "ikromjon2@gmail.com"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "ikromjon",
                "first_name": "Ikromjon",
                "last_name": "Ergashev",
                "email": "invalid-email",
                "password": "somepassword"
            }
        )

        user_count = CustomUser.objects.count()

        self.assertEqual(user_count, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = CustomUser.objects.create(username="ikromjon", first_name="Ikromjon")
        user.set_password("somepass")
        user.save()

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "ikromjon",
                "first_name": "Ikromjon",
                "last_name": "Ergashev",
                "email": "ikromjon2@gmail.com",
                "password": "somepassword"
            }
        )

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, "form", "username", "A user with that username already exists.")



class LoginTestCase(TestCase):
    # DRY - Don't Repeat Yourself
    def setUp(self):
        self.db_user = CustomUser.objects.create(username="ikromjon", first_name="Ikromjon")
        self.db_user.set_password("somepassword")
        self.db_user.save()
    def test_successful_login(self):

        self.client.post(
            reverse("users:login"),
            data={
                'username': "ikromjon",
                "password": "somepassword"
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_login(self):
        self.client.post(
            reverse("users:login"),
            data = {
                'username': "wrong-username",
                'password': "somepassword"
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        self.client.post(
            reverse("users:login"),
            data = {
                'username': "ikromjon",
                'password': "wrong-password"
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username="ikromjon", password="somepassword")
        self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)



class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.url, reverse("users:login"))
        self.assertEqual(response.url, reverse("users:login")+'?next=/users/profile/')

    def test_profile_detail(self):
        user = CustomUser.objects.create(username="ikromjon",
                                   first_name="Ikromjon",
                                   last_name="Ergashev",
                                   email="ikromjon@gmail.com")

        user.set_password("<PASSWORD>")
        user.save()

        self.client.login(username="ikromjon", password="<PASSWORD>")

        response = self.client.get(reverse("users:profile"))

        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = CustomUser.objects.create(username="ikromjon",
                                   first_name="Ikromjon",
                                   last_name="Ergashev",
                                   email="ikromjon@gmail.com")
        user.set_password("<PASSWORD>")
        user.save()

        self.client.login(username="ikromjon", password="<PASSWORD>")

        response = self.client.post(
            reverse("users:profile-edit"),
            data={
                "username": "ikromjon",
                "first_name": "Ikromjon",
                "last_name": "John",
                "email": "ikromjon1@gmail.com",
            })

        # user = CustomUser.objects.get(pk=user.pk)
        user.refresh_from_db()

        # self.assertEqual(user.last_name, 'John')
        self.assertEqual(user.email, 'ikromjon1@gmail.com')
        self.assertEqual(response.url, reverse('users:profile'))

