# Generated by Django 3.2.1 on 2021-12-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0010_alter_inventory_in_stock_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='buy_price',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='sell_price',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
