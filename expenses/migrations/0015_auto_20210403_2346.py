# Generated by Django 3.1.4 on 2021-04-03 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0014_auto_20210403_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryitem',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='expenses.account'),
        ),
    ]