# Generated by Django 4.1.4 on 2022-12-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='authot',
            new_name='author',
        ),
    ]
