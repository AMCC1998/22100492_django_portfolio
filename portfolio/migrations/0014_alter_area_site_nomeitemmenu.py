# Generated by Django 4.2.1 on 2023-06-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_area_site_nomeitemmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area_site',
            name='nomeItemMenu',
            field=models.CharField(default='', max_length=50),
        ),
    ]