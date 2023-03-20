# Generated by Django 4.1.7 on 2023-03-09 07:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('phonenum', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]