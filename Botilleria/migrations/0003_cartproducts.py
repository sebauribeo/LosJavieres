# Generated by Django 4.1.2 on 2022-10-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0002_product_image_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=500)),
            ],
        ),
    ]
