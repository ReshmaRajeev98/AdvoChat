# Generated by Django 3.2.15 on 2022-09-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawsdb',
            name='desc',
            field=models.TextField(default='', max_length=800),
        ),
        migrations.AlterField(
            model_name='lawsdb',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
