# Generated by Django 4.0.4 on 2022-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_categoria_options_categoria_creado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
