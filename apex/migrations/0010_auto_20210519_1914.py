# Generated by Django 3.2.2 on 2021-05-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex', '0009_auto_20210515_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Name',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='UserName',
            new_name='First_Name',
        ),
        migrations.AddField(
            model_name='register',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]