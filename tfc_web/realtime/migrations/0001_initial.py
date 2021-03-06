# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('atco_code', models.CharField(max_length=12)),
                ('naptan_code', models.CharField(max_length=8)),
                ('plate_code', models.CharField(max_length=10)),
                ('cleardown_code', models.CharField(max_length=10)),
                ('common_name', models.CharField(max_length=64)),
                ('common_name_lang', models.CharField(max_length=2)),
                ('short_common_name', models.CharField(max_length=21)),
                ('short_common_name_lang', models.CharField(max_length=2)),
                ('landmark', models.CharField(max_length=64)),
                ('landmark_lang', models.CharField(max_length=2)),
                ('street', models.CharField(max_length=64)),
                ('street_lang', models.CharField(max_length=2)),
                ('crossing', models.CharField(max_length=64)),
                ('crossing_lang', models.CharField(max_length=2)),
                ('indicator', models.CharField(max_length=64)),
                ('indicator_lang', models.CharField(max_length=2)),
                ('bearing', models.CharField(max_length=2)),
                ('nptg_locality_code', models.CharField(max_length=8)),
                ('locality_name', models.CharField(max_length=64)),
                ('parent_locality_name', models.CharField(max_length=64)),
                ('grand_parent_locality_name', models.CharField(max_length=64)),
                ('town', models.CharField(max_length=64)),
                ('town_lang', models.CharField(max_length=2)),
                ('suburb', models.CharField(max_length=64)),
                ('suburb_lang', models.CharField(max_length=2)),
                ('locality_centre', models.BooleanField()),
                ('grid_type', models.CharField(max_length=1)),
                ('easting', models.IntegerField()),
                ('northing', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('stop_type', models.CharField(max_length=3)),
                ('bus_stop_type', models.CharField(max_length=3)),
                ('timing_status', models.CharField(max_length=3)),
                ('default_wait_time', models.IntegerField()),
                ('notes', models.CharField(max_length=255)),
                ('notes_lang', models.CharField(max_length=2)),
                ('administrative_area_code', models.IntegerField()),
                ('creation_datetime', models.DateTimeField()),
                ('modification_datetime', models.DateTimeField()),
                ('revision_number', models.IntegerField()),
                ('modification', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=3)),
            ],
        ),
    ]
