# Generated by Django 3.1.4 on 2021-03-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_entryitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
