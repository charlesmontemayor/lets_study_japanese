# Generated by Django 3.0.5 on 2020-07-23 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='forum',
            old_name='user',
            new_name='author',
        ),
    ]
