# Generated by Django 3.1.4 on 2021-03-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
