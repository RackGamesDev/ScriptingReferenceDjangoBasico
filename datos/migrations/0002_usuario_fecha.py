# Generated by Django 4.2.11 on 2024-09-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
