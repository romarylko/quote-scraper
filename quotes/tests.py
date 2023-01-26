from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from quotes.models import Author, Tag, Quote


class AuthorTestCase(APITestCase):

    def setUp(self) -> None:
        Author.objects.bulk_create([
            Author(name='Albert Einstein'),
            Author(name='J.K. Rowling'),
            Author(name='Jane Austen'),
            Author(name='Marilyn Monroe')
        ])

    def test_author_list_url(self):
        url = reverse('quotes:author-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authors_count(self):
        url = reverse('quotes:author-list')
        response = self.client.get(path=url)
        self.assertEqual(len(response.data['results']), Author.objects.count())

    def test_single_author(self):
        url = reverse('quotes:author-detail', kwargs={'pk': 1})
        response = self.client.get(path=url)
        self.assertEqual(response.data, {'id': 1, 'name': 'Albert Einstein'})


class TagTestCase(APITestCase):

    def setUp(self) -> None:
        Tag.objects.bulk_create([
            Tag(name='change'),
            Tag(name='deep-thoughts'),
            Tag(name='world')
        ])

    def test_tag_list_url(self):
        url = reverse('quotes:tag-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tags_count(self):
        url = reverse('quotes:tag-list')
        response = self.client.get(path=url)
        self.assertEqual(len(response.data['results']), Tag.objects.count())

    def test_single_tag(self):
        url = reverse('quotes:tag-detail', kwargs={'pk': 3})
        response = self.client.get(path=url)
        self.assertEqual(response.data, {'id': 3, 'name': 'world'})


class QuoteTestCase(APITestCase):

    def setUp(self) -> None:
        self.tag1 = Tag.objects.create(name='inspirational')
        self.tag2 = Tag.objects.create(name='love')
        self.tag3 = Tag.objects.create(name='life')
        self.author1 = Author.objects.create(name='Albert Einstein')
        self.author2 = Author.objects.create(name='André Gide')
        self.quote1 = Quote.objects.create(
            text='“It is better to be hated for what you are than to be loved for what you are not.”',
            author=self.author2,
        )
        self.quote2 = Quote.objects.create(
            text='“There are only two ways to live your life. One is as though nothing is a miracle. '
                 'The other is as though everything is a miracle.”',
            author=self.author1
        )
        self.quote1.tags.add(self.tag2)
        self.quote1.tags.add(self.tag3)
        self.quote2.tags.add(self.tag1)
        self.quote2.tags.add(self.tag3)

    def test_quote_list_url(self):
        url = reverse('quotes:quote-list')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_quotes_count(self):
        url = reverse('quotes:quote-list')
        response = self.client.get(path=url)
        self.assertEqual(len(response.data['results']), Quote.objects.count())
