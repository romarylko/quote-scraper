from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from quotes.models import Author, Tag, Quote
from quotes.serializers import AuthorSerializer, TagSerializer, QuoteSerializer


class QuoteViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class TagViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class AuthorViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
