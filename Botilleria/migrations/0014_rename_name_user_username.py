# Generated by Django 4.1.2 on 2022-11-27 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0013_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]