# Generated by Django 3.2.7 on 2021-09-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializator', '0002_auto_20210916_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meteor',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
