# Generated by Django 4.0.6 on 2022-07-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_news_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(default='Noticia', max_length=500),
        ),
    ]
