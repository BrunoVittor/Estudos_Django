# Generated by Django 2.1.15 on 2020-11-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='creation',
            field=models.DateTimeField(),
        ),
    ]
