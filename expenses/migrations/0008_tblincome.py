# Generated by Django 5.0.1 on 2024-08-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_remove_tblexpenses_currency_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblIncome',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('source_id', models.IntegerField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]