# Generated by Django 4.1.4 on 2023-02-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0010_alter_data_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]