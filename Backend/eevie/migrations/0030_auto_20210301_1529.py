# Generated by Django 3.1.4 on 2021-03-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eevie', '0029_remove_session_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='provider',
        ),
        migrations.AddField(
            model_name='session',
            name='provider',
            field=models.ManyToManyField(null=True, related_name='sessions', to='eevie.Provider'),
        ),
    ]