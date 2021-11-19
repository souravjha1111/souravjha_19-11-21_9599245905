# Generated by Django 3.2.3 on 2021-11-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(upload_to='api')),
            ],
        ),
        migrations.CreateModel(
            name='valueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=13)),
            ],
        ),
    ]
