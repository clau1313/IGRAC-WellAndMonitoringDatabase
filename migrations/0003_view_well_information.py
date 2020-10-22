# Generated by Django 2.2.12 on 2020-07-03 09:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('gwml2', '0002_initial_term_data'),
    ]

    sql = """
       CREATE VIEW well_information AS
select w.id,
       w.id                                                           as "ggis_id",
       w.original_id                                                  as "original_id",
       w.name                                                         as "name",
       c.name                                                         as "country",
       type.name                                                      as "feature_type",
       hydro.aquifer_name                                             as "aquifer_name",
       concat('<a href="/groundwater/well/', w.id, '/edit">edit</a>') as "editor",
       w.location
From well as w
       LEFT JOIN country c on w.country_id = c.id
       LEFT JOIN term_feature_type type on w.feature_type_id = type.id
       LEFT JOIN hydrogeology_parameter as hydro on w.hydrogeology_parameter_id = hydro.id;
        """

    operations = [
        migrations.RunSQL('DROP VIEW IF EXISTS well_information;'),
        migrations.RunSQL(sql)
    ]
