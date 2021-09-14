# Generated by Django 3.2.2 on 2021-05-13 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='essentialitemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=40)),
                ('Date', models.DateField(max_length=40)),
                ('Size', models.CharField(max_length=40)),
                ('Qauntity', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='LogTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('CRUPoperation', models.CharField(max_length=40)),
                ('TableName', models.CharField(max_length=40)),
                ('Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='processingCoil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialType', models.CharField(blank=True, max_length=40, null=True)),
                ('Qauntity', models.CharField(blank=True, max_length=40, null=True)),
                ('Thickness', models.CharField(blank=True, max_length=40)),
                ('Size', models.CharField(blank=True, max_length=40)),
                ('Weight', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='rawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('Thickness', models.CharField(max_length=40)),
                ('Size', models.CharField(max_length=40)),
                ('Grade', models.CharField(max_length=40)),
                ('coilWeight', models.CharField(max_length=40)),
                ('scrapWeight', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UFMstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialType', models.CharField(max_length=40)),
                ('Thickness', models.CharField(max_length=40)),
                ('Size', models.CharField(max_length=40)),
                ('Weight', models.CharField(max_length=40)),
                ('Qauntity', models.CharField(max_length=40)),
                ('UFMcoilUID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.processingcoil')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('UserName', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='processingcoil',
            name='rewMaterial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.rawmaterial'),
        ),
        migrations.CreateModel(
            name='FMstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialType', models.CharField(max_length=40)),
                ('Thickness', models.CharField(max_length=40)),
                ('Size', models.CharField(max_length=40)),
                ('Weight', models.CharField(max_length=40)),
                ('Qauntity', models.CharField(max_length=40)),
                ('coilUID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.processingcoil')),
            ],
        ),
        migrations.CreateModel(
            name='FMsell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materialType', models.CharField(max_length=40)),
                ('Thickness', models.CharField(max_length=40)),
                ('Size', models.CharField(max_length=40)),
                ('Weight', models.CharField(max_length=40)),
                ('Qauntity', models.CharField(max_length=40)),
                ('FMcoilUID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.fmstock')),
            ],
        ),
        migrations.CreateModel(
            name='EssentialItemUsePerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=40, null=True)),
                ('Size', models.CharField(blank=True, max_length=40, null=True)),
                ('Date', models.DateTimeField()),
                ('Qauntity', models.CharField(max_length=40)),
                ('EsstentialItemUID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.essentialitemstock')),
            ],
        ),
    ]