# Generated by Django 2.0.7 on 2018-07-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0010_auto_20180724_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nivelAcesso',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
