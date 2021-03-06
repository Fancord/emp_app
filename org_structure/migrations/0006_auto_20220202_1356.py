# Generated by Django 3.2.11 on 2022-02-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_structure', '0005_alter_position_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='position',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
