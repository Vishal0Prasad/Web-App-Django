# Generated by Django 2.1.2 on 2018-10-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0005_auto_20181025_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='messrefund',
            name='account_holder_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='messrefund',
            name='account_number',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='messrefund',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='messrefund',
            name='refund_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messrefund',
            name='refund_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messfeedback',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-10-25 21:45:56.277619'),
        ),
    ]
