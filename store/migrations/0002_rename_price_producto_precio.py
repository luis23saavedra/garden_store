# Generated by Django 4.0.4 on 2022-04-28 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='price',
            new_name='precio',
        ),
    ]
