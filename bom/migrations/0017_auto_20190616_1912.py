# Generated by Django 2.2 on 2019-06-16 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0016_auto_20190405_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PartChangeHistory',
            new_name='PartRevision',
        ),
    ]
