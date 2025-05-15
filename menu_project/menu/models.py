from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['title']

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        related_name='items',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский пункт меню',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    title = models.CharField('Название', max_length=100)
    url = models.CharField('Ссылка или named url', max_length=200, blank=True)
    is_named_url = models.BooleanField('named url', default=False)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['parent__id', 'title']
        unique_together = ('menu', 'parent', 'title')

    def clean(self):
        if not self.is_named_url and self.url:
            if not self.url.startswith('/'):
                self.url = '/' + self.url
            if not self.url.endswith('/'):
                self.url += '/'

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        from django.urls import NoReverseMatch, reverse
        if self.is_named_url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return '#'
        return self.url or '#'
