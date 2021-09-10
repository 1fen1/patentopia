# Generated by Django 3.2.4 on 2021-07-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Результат поиска', max_length=100)),
                ('link', models.CharField(help_text='Ссылка на результат поиска', max_length=100)),
                ('search_imput', models.CharField(help_text='Введенный поисковый запрос', max_length=100)),
            ],
        ),
    ]
