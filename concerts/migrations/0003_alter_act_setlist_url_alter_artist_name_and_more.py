# Generated by Django 4.1.4 on 2022-12-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0002_rename_date_concert_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='setlist_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='concert',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]