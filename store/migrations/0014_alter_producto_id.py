# Generated by Django 4.0.4 on 2022-05-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_producto_id_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.IntegerField(blank=True, default=0, null=True, primary_key=True, serialize=False),
        ),
    ]