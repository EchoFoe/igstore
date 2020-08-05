# Generated by Django 3.0.6 on 2020-07-28 12:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0003_order_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Тип эл. адреса')),
                ('is_active', models.BooleanField(default=True, verbose_name='Акутальность')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тип е-мейла',
                'verbose_name_plural': 'Типы е-мейлов',
            },
        ),
        migrations.CreateModel(
            name='EmailSendingFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, verbose_name='Электронный адрес')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата ред-ия записи')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailType', verbose_name='Тип эл. адреса')),
            ],
            options={
                'verbose_name': 'Отправленный е-мейл',
                'verbose_name_plural': 'Отправленные е-мейлы',
            },
        ),
    ]