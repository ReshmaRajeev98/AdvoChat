# Generated by Django 3.2.15 on 2022-10-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0013_alter_bookdb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyerdb',
            name='reason_l',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='lawyerdb',
            name='status_l',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
