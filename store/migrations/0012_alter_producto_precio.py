# Generated by Django 4.0.4 on 2022-05-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_producto_id_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]