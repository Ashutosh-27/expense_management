# Generated by Django 5.0.1 on 2024-08-25 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblexpenses',
            name='currency_id',
        ),
    ]
