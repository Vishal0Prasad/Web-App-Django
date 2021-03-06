# Generated by Django 2.1.2 on 2018-10-25 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181025_1609'),
        ('mess', '0003_messitems_orderhistorymess_orderlistmess'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=256, null=True)),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('comp_img', models.ImageField(blank=True, null=True, upload_to='images/2018-10-25 15:07:00.876792')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Student')),
            ],
        ),
    ]
