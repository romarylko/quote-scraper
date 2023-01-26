from quotes.models import Author, Quote, Tag


class SaveQuotePipeline:
    """Pipeline for saving quote in database"""

    def process_item(self, item, spider):
        quote = Quote.objects.filter(text=item['text']).first() or Quote()
        author, _ = Author.objects.get_or_create(name=item['author'])
        quote.text = item['text']
        quote.author = author
        quote.save()

        for tag_name in item.get('tags', []):
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            quote.tags.add(tag)
        return item
