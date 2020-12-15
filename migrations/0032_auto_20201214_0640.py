# Generated by Django 2.2.12 on 2020-12-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gwml2', '0031_well_public'),
    ]

    operations = [
        migrations.RunSQL('DROP VIEW IF EXISTS well_with_uuid;'),
        migrations.RunSQL('DROP VIEW IF EXISTS well_information_uuid;'),
        migrations.RunSQL('DROP VIEW IF EXISTS well_information;'),
        migrations.AlterField(
            model_name='construction',
            name='pump_installer',
            field=models.CharField(blank=True, help_text='Name of the company or person who installed the pump.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='constructionstructure',
            name='material',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='manager',
            field=models.CharField(blank=True, help_text='Name of the manager or owner of the groundwater point. This can be a single person, a group of persons or an organisation.', max_length=200, null=True,
                                   verbose_name='Manager / owner'),
        ),
        migrations.AlterField(
            model_name='stratigraphiclog',
            name='material',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stratigraphiclog',
            name='stratigraphic_unit',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='well',
            name='original_id',
            field=models.CharField(help_text='As recorded in the original database.', max_length=20),
        ),
        migrations.AlterField(
            model_name='welllevelmeasurement',
            name='methodology',
            field=models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wellqualitymeasurement',
            name='methodology',
            field=models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='wellyieldmeasurement',
            name='methodology',
            field=models.CharField(blank=True, help_text='Explain the methodology used to collect the data, in the field and eventually in the lab.', max_length=200, null=True),
        ),
    ]