# Generated by Django 3.0.5 on 2020-06-10 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0002_auto_20200608_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guide',
            options={'ordering': ['-date']},
        ),
    ]
