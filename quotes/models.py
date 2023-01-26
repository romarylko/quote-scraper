from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Author(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Quote(models.Model):
    text = models.TextField()

    author = models.ForeignKey(
        to=Author,
        verbose_name=_('author'),
        related_name='quotes',
        related_query_name='quotes',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name=_('author'),
        related_name='quotes',
        related_query_name='quotes',
    )

    def __str__(self):
        return f'{self.author}: {" ".join(self.text.split()[:5])}...'

    class Meta:
        ordering = ('author',)
