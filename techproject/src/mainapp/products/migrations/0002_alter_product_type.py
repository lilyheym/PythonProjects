# Generated by Django 4.2.6 on 2023-10-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
