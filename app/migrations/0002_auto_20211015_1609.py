# Generated by Django 3.2.7 on 2021-10-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeequipment',
            name='borrowed_by',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='officeequipment',
            name='borrowed_since',
            field=models.TextField(),
        ),
    ]
