# Generated by Django 5.0.1 on 2024-08-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_alter_category_u_id_alter_source_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblexpenses',
            name='datetime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tblincome',
            name='datetime',
            field=models.DateField(),
        ),
    ]
