# Generated by Django 4.1.2 on 2022-11-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Botilleria', '0018_remove_user_role_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
