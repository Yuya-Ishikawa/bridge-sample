# Generated by Django 2.1.2 on 2018-10-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=100)),
                ('pageUrl', models.CharField(max_length=100)),
                ('tips', models.CharField(max_length=200)),
                ('content1', models.CharField(max_length=500)),
                ('content2', models.CharField(max_length=500)),
                ('content3', models.CharField(max_length=500)),
                ('content4', models.CharField(max_length=500)),
                ('publishDay', models.DateField()),
            ],
        ),
    ]