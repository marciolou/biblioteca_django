# Generated by Django 4.1.5 on 2023-01-21 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 9, 46, 47, 648696)),
        ),
    ]
