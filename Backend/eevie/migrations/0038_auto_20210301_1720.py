# Generated by Django 3.1.4 on 2021-03-01 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eevie', '0037_auto_20210301_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='points', to='eevie.station'),
        ),
    ]
