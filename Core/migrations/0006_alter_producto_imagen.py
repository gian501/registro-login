# Generated by Django 4.1.7 on 2023-03-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
