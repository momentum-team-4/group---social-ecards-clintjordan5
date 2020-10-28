# Generated by Django 3.1.2 on 2020-10-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_followedusers_followed_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='border',
            field=models.CharField(choices=[('solid', 'solid'), ('dotted', 'dotted'), ('none', 'none'), ('', '')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('blue', 'blue'), ('red', 'red'), ('none', 'none'), ('', '')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Times New Roman', 'Times New Roman'), ('Helvetica', 'Helvetica'), ('Open Sans', 'Open Sans'), ('none', 'none'), ('', '')], default='', max_length=100, null=True),
        ),
    ]