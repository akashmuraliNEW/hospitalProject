# Generated by Django 4.2.3 on 2024-09-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]
