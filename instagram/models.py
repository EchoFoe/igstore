from django.db import models
from django.utils import timezone


# Фотографии к инстаграму:
class ImageItem(models.Model):
    image = models.ImageField(upload_to='instagram/%Y/%m/%d', verbose_name='Фотография',
                              help_text='Фотография должна иметь размеры 300x400 px для корректного отображения на сайте!')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата ред-ия записи')

    class Meta:
        verbose_name = 'Фотография к инстаграму'
        verbose_name_plural = 'Фотографии к инстаграму'

    def __str__(self):
        return '%s' % self.image
