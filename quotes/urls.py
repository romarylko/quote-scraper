from rest_framework import routers

from quotes.views import AuthorViewSet, TagViewSet, QuoteViewSet

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet, 'author')
router.register('quotes', QuoteViewSet, 'quote')
router.register('tags', TagViewSet, 'tag')

app_name = 'quotes'

urlpatterns = router.urls
