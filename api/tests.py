from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from books.models import Book, BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="ikromjon", first_name="Ikromjon")
        self.user.set_password("somepassword")
        self.user.save()
        self.client.login(username='ikromjon', password='somepassword')


    def test_book_review_details(self):
        book1 = Book.objects.create(title="Sport", description="Description1", isbn="123121")
        br = BookReview.objects.create(book=book1, stars_given=5, user=self.user, comment='Very good book')

        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id}))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], 'Very good book')
        self.assertEqual(response.data['user']['id'], 1)
        self.assertEqual(response.data['user']['username'], 'ikromjon')
        self.assertEqual(response.data['user']['first_name'], 'Ikromjon')
        self.assertEqual(response.data['book']['id'], 1)
        self.assertEqual(response.data['book']['title'], 'Sport')
        self.assertEqual(response.data['book']['description'], 'Description1')
        self.assertEqual(response.data['book']['isbn'], '123121')

    def test_book_review_list(self):
        user_two = CustomUser.objects.create(username="somebody", first_name="Somebody")
        book1 = Book.objects.create(title="Sport", description="Description1", isbn="123121")
        br = BookReview.objects.create(book=book1, stars_given=5, user=self.user, comment='Very good book')
        br_two = BookReview.objects.create(book=book1, stars_given=2, user=user_two, comment='Not bad')

        response = self.client.get(reverse('api:review-list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['count'], 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(response.data['results'][0]['id'], br_two.id)
        self.assertEqual(response.data['results'][0]['stars_given'], br_two.stars_given)
        self.assertEqual(response.data['results'][0]['comment'], br_two.comment)
        self.assertEqual(response.data['results'][1]['id'], br.id)
        self.assertEqual(response.data['results'][1]['stars_given'], br.stars_given)
        self.assertEqual(response.data['results'][1]['comment'], br.comment)