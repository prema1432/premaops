# Generated by Django 2.2.6 on 2020-05-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OPSApp', '0002_auto_20200527_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupload',
            name='ptype',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
