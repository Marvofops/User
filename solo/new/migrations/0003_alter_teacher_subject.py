# Generated by Django 5.1.6 on 2025-03-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
