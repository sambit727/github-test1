# Generated by Django 3.1.4 on 2021-03-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_auto_20210315_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
