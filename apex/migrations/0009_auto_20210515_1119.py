# Generated by Django 3.2.2 on 2021-05-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0008_auto_20210515_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtable',
            name='Table_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='essentialitemuseperday',
            name='EPD_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='Log_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='RM_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
