# Generated by Django 3.2.15 on 2022-09-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_r', models.CharField(max_length=20)),
                ('phone_r', models.IntegerField()),
                ('enr_r', models.IntegerField()),
                ('email_r', models.CharField(max_length=20)),
                ('pwd_r', models.CharField(max_length=20)),
            ],
        ),
    ]
