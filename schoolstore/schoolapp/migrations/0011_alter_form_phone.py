# Generated by Django 4.1.3 on 2023-06-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0010_alter_form_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='phone',
            field=models.IntegerField(max_length=50),
        ),
    ]
