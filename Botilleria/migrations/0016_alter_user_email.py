# Generated by Django 4.1.2 on 2022-11-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0015_user_name_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
