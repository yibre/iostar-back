# Generated by Django 2.2.5 on 2021-12-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211116_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]