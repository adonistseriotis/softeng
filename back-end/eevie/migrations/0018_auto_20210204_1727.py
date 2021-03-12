# Generated by Django 3.1.4 on 2021-02-04 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eevie', '0017_auto_20210204_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='photo',
        ),
        migrations.CreateModel(
            name='MediaTypes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('itemUrl', models.URLField(null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediaItems', to='eevie.station')),
            ],
        ),
    ]