# Generated by Django 5.1.6 on 2025-03-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=2)),
                ('age', models.CharField(max_length=2)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
