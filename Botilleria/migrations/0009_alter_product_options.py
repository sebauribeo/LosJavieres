# Generated by Django 4.1.2 on 2022-10-25 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0008_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]