# Generated by Django 4.2.1 on 2023-06-03 10:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_remove_area_site_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_site',
            name='html',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]