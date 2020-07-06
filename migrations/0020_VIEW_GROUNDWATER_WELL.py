# Generated by Django 2.2.12 on 2020-07-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('gwml2', '0019_auto_20200703_0903'),
    ]

    sql = """
        CREATE VIEW groundwater_well AS 
        select id, gw_well_name AS well_name, gw_well_total_length AS well_total_length, gw_well_location from gwml2_gwwell;
        """

    operations = [
        migrations.RunSQL('DROP VIEW IF EXISTS groundwater_well;'),
        migrations.RunSQL(sql)
    ]
