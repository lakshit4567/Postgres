# Generated by Django 3.2.2 on 2021-05-13 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sale_Type', models.CharField(blank=True, max_length=40, null=True)),
                ('Sale_date', models.DateField(blank=True, null=True)),
                ('Sale_Weight', models.CharField(blank=True, max_length=40, null=True)),
                ('Sale_Quantity', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='processingcoil',
            name='rewMaterial',
        ),
        migrations.RenameField(
            model_name='essentialitemuseperday',
            old_name='Size',
            new_name='EPD_Quantity',
        ),
        migrations.RenameField(
            model_name='essentialitemuseperday',
            old_name='Type',
            new_name='EPD_Size',
        ),
        migrations.RenameField(
            model_name='essentialitemuseperday',
            old_name='EsstentialItemUID',
            new_name='EPD_UID',
        ),
        migrations.RemoveField(
            model_name='essentialitemstock',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='essentialitemstock',
            name='Qauntity',
        ),
        migrations.RemoveField(
            model_name='essentialitemstock',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='essentialitemuseperday',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='essentialitemuseperday',
            name='Qauntity',
        ),
        migrations.RemoveField(
            model_name='fmstock',
            name='Qauntity',
        ),
        migrations.RemoveField(
            model_name='fmstock',
            name='Thickness',
        ),
        migrations.RemoveField(
            model_name='fmstock',
            name='Weight',
        ),
        migrations.RemoveField(
            model_name='logtable',
            name='CRUPoperation',
        ),
        migrations.RemoveField(
            model_name='logtable',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='Grade',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='Thickness',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='coilWeight',
        ),
        migrations.RemoveField(
            model_name='rawmaterial',
            name='scrapWeight',
        ),
        migrations.RemoveField(
            model_name='register',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='Qauntity',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='Thickness',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='UFMcoilUID',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='Weight',
        ),
        migrations.RemoveField(
            model_name='ufmstock',
            name='materialType',
        ),
        migrations.AddField(
            model_name='essentialitemstock',
            name='ES_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='essentialitemstock',
            name='ES_Quantity',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='essentialitemstock',
            name='ES_Size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='essentialitemstock',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='essentialitemuseperday',
            name='EPD_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='essentialitemuseperday',
            name='EPD_Type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='essentialitemuseperday',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_Quantity',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_Size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_Thickness',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_Weight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='FM_scrapWeight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='Grade',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='UF_Quantity',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='UF_Size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='UF_Thickness',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='UF_Weight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='coilWeight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fmstock',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='logtable',
            name='CRUDoperation',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='logtable',
            name='Log_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logtable',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_Grade',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_Size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_Thickness',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_coilWeight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='RM_scrapWeight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='userRole',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ufmstock',
            name='FMid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.fmstock'),
        ),
        migrations.AddField(
            model_name='ufmstock',
            name='UFM_Quantity',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ufmstock',
            name='UFM_Weight',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ufmstock',
            name='UFM_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ufmstock',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='essentialitemstock',
            name='Type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fmstock',
            name='Size',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='fmstock',
            name='coilUID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='fmstock',
            name='materialType',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='TableName',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='logtable',
            name='username',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='Name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='UserName',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='FMsell',
        ),
        migrations.DeleteModel(
            name='processingCoil',
        ),
        migrations.AddField(
            model_name='sale',
            name='FMcoilUID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apex.fmstock'),
        ),
        migrations.AddField(
            model_name='sale',
            name='register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
