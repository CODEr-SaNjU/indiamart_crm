# Generated by Django 3.1.3 on 2020-11-09 06:45

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Crm_app', '0003_userreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='MobNum',
            field=phone_field.models.PhoneField(help_text='Contact number', max_length=31),
        ),
    ]