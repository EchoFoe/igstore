# Generated by Django 3.0.6 on 2020-07-29 11:23

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200727_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('-name',), 'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeManyToManyField(blank=True, related_name='products', to='products.ProductCategory', verbose_name='Категория'),
        ),
    ]
