# Generated by Django 2.2.6 on 2020-06-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OPSApp', '0007_auto_20200604_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupload',
            name='gucomments',
            field=models.TextField(default=' No Comments '),
        ),
        migrations.AlterField(
            model_name='pupload',
            name='hocomments',
            field=models.TextField(default=' No Comments '),
        ),
        migrations.AlterField(
            model_name='pupload',
            name='rating',
            field=models.IntegerField(default='3', max_length=250),
        ),
    ]
