# Generated by Django 3.2.9 on 2021-12-06 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_rename_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]