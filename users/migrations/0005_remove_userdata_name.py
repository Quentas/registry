# Generated by Django 3.2.7 on 2021-09-06 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210906_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
    ]
