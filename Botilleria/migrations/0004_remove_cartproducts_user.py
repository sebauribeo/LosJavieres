# Generated by Django 4.1.2 on 2022-10-23 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0003_cartproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproducts',
            name='user',
        ),
    ]
