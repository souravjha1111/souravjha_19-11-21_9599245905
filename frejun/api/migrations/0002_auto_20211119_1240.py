# Generated by Django 3.2.3 on 2021-11-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='csv',
            new_name='csvmodel',
        ),
        migrations.AlterField(
            model_name='valuemodel',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]
