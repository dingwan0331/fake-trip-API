# Generated by Django 4.0.5 on 2022-07-08 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomimage',
            name='product',
        ),
        migrations.AddField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.room'),
        ),
    ]
