# Generated by Django 4.1.4 on 2022-12-30 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='concert',
            name='setlist_url',
        ),
        migrations.AddField(
            model_name='concert',
            name='end_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='concert',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setlist_url', models.CharField(max_length=400)),
                ('is_main', models.BooleanField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts.artist')),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concerts.concert')),
            ],
        ),
    ]
