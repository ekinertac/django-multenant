# Generated by Django 2.2.4 on 2019-08-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multenant', '0002_auto_20190813_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='unique_key',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]
