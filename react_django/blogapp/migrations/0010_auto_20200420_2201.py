# Generated by Django 2.1.5 on 2020-04-20 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_auto_20191021_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
