# Generated by Django 4.1.2 on 2022-10-24 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0006_alter_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
