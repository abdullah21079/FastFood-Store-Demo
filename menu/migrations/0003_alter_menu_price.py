# Generated by Django 5.0.3 on 2024-04-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
    ]
