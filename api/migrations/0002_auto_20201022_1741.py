# Generated by Django 3.1.2 on 2020-10-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
