# Generated by Django 3.2.1 on 2021-12-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeebank',
            name='added_on',
            field=models.DateTimeField(),
        ),
    ]
