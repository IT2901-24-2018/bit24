# Generated by Django 2.0.2 on 2018-05-02 10:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_merge_20180418_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField(help_text='When the weather data was generated. Example: 2018-12-09T08:45:15Z')),
                ('county_and_municipality_id', models.IntegerField(help_text='County and municipality number put together.Example: 5001 for Trondheim')),
                ('value', models.IntegerField(help_text='The amount of precipitation without the unit. Example: 2')),
                ('unit', models.CharField(help_text='The unit describing the value. Max two in length. Example: mm for millimeter', max_length=2)),
                ('degrees', models.IntegerField(help_text='The degree measured in celsius.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='brush_active',
            field=models.NullBooleanField(help_text='Brush boolean. Optional.'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='dry_spreader_active',
            field=models.NullBooleanField(help_text='Dry spreader active boolean. Optional.'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='endlat',
            field=models.FloatField(help_text='End latitude. Example: 63.3874419990294'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='endlong',
            field=models.FloatField(help_text='End longitude. Example: 10.3290930003037'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='material_type_code',
            field=models.IntegerField(help_text='Material type boolean. Optional', null=True),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='plow_active',
            field=models.NullBooleanField(help_text='Plow boolean. Optional.'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='segment',
            field=models.ForeignKey(help_text='Segment ID to mapped segment. Will be autocompleted by the code. Enter dummy value.', on_delete=django.db.models.deletion.CASCADE, to='api.RoadSegment'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='startlat',
            field=models.FloatField(help_text='Start latitude. Example: 63.3870750023729'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='startlong',
            field=models.FloatField(help_text='Start longitute. Example: 10.3277250005425'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='time',
            field=models.DateTimeField(help_text='When the production data was generated. Example: 2016-11-04T08:45:15Z'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='wet_spreader_active',
            field=models.NullBooleanField(help_text='Wet spreader boolean. Optional.'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='category',
            field=models.CharField(help_text='Road segment category. Example: K', max_length=4),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='county',
            field=models.IntegerField(help_text='County identifier.  Example: 50'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='href',
            field=models.CharField(help_text='Link to NVDB for this unique segment', max_length=150),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='municipality',
            field=models.IntegerField(help_text='Municipality number for that county.Example: 01 for Trondheim'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='region',
            field=models.IntegerField(help_text='Region number. Example: 4'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='roadsectionid',
            field=models.IntegerField(help_text='Unique identifier for the road segment. Example: 171712'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='startdate',
            field=models.DateField(help_text='Start date for the road segment. Example: 2018-04-20'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='status',
            field=models.CharField(help_text='Road status. Example: G', max_length=4),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='stretchdistance',
            field=models.IntegerField(help_text='Length of the road segment. Example 31'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.LineStringField(help_text='Linestring according to ISO 19162:2015. Example: SRID=4326;LINESTRING (10.37634290477487 63.3478716972899, 10.37656821856063 63.34786722088941)', srid=4326),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='typeofroad',
            field=models.CharField(help_text='A description of the road type. Example: gangOgSykkelvei', max_length=100),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='vrefshortform',
            field=models.CharField(help_text='A combination of multiple fields. Example: 5001 Kg97587 hp1 m349-380', max_length=255),
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='segment',
            field=models.ForeignKey(help_text='Segment ID to mapped segment. Will be autocompleted by the code. Enter dummy value.', on_delete=django.db.models.deletion.CASCADE, to='api.RoadSegment'),
        ),
    ]
