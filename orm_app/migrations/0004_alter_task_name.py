# Generated by Django 5.1rc1 on 2024-08-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]