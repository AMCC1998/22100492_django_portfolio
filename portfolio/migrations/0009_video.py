# Generated by Django 4.2.1 on 2023-06-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_foto_options_alter_foto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('iframe', models.TextField(max_length=2000)),
            ],
        ),
    ]