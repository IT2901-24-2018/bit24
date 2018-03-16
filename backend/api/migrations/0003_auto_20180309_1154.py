# Generated by Django 2.0.2 on 2018-03-09 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180309_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='productiondata',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 9, 11, 54, 19, 786156)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='materialtype_kode',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='plogaktiv',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='torrsprederaktiv',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='vatsprederaktiv',
            field=models.NullBooleanField(),
        ),
    ]