# Generated by Django 4.2.1 on 2023-06-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_area_site_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_site',
            name='posicao',
            field=models.IntegerField(default=0),
        ),
    ]
