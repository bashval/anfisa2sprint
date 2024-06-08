from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
        )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обертки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'


class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория',
    )
    toppings = models.ManyToManyField(
        Topping,
        verbose_name='Топпинги'
        )
    is_on_main = models.BooleanField(default=False, verbose_name='На главную')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
        ordering = ('output_order',)
