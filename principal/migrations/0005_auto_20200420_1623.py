# Generated by Django 3.0.5 on 2020-04-20 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_grupo_numero_grp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personas',
            name='division',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='grupo',
        ),
    ]