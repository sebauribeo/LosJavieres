# Generated by Django 4.1.2 on 2022-11-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0020_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]