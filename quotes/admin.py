from django.contrib import admin

from quotes.models import Author, Tag, Quote


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_text', 'author', 'get_tags')
    list_display_links = ('id', 'get_text')
    list_filter = ('author',)
    search_fields = ('text',)

    def get_tags(self, quote):
        return ', '.join(x.name for x in quote.tags.all())

    get_tags.short_description = 'tags'

    def get_text(self, quote):
        return f'{quote.text[:50]}...'

    get_text.short_description = 'text'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quote, QuoteAdmin)
