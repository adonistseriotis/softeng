# Generated by Django 3.1.4 on 2021-01-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eevie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_no',
            field=models.IntegerField(),
        ),
    ]
