# Generated by Django 2.2.12 on 2020-11-17 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0014_auto_20201117_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='license',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.License'),
        ),
    ]