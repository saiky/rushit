# Generated by Django 4.2.4 on 2023-09-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='isd_code',
            field=models.IntegerField(),
        ),
    ]
