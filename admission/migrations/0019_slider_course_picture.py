# Generated by Django 4.1.7 on 2023-04-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0018_bachelorsintheology_certificateintheology_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='sliderpics')),
                ('caption', models.TextField(default='keep the content short')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='picture',
            field=models.ImageField(default='', upload_to='coursepic'),
        ),
    ]