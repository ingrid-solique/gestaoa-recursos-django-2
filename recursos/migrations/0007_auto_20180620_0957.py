# Generated by Django 2.0.1 on 2018-06-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20180620_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=500),
        ),
    ]
