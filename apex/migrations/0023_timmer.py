# Generated by Django 3.2.2 on 2021-05-30 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0022_auto_20210529_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_time', models.CharField(blank=True, max_length=40, null=True)),
                ('inactive_time', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]