from django.db import models
from django.utils import timezone


class Review(models.Model):
    first_name = models.CharField(max_length=32, verbose_name='Имя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    image = models.ImageField(upload_to='review/%Y/%m/%d', verbose_name='Фотография',
                              help_text='Фотография должна иметь размеры 60px x 60px для корректного отображения на сайте!')
    message = models.TextField(max_length=2048, verbose_name='Отзыв')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность отзыва')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return "%s" % self.first_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
