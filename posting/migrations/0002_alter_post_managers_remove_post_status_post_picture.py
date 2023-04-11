# Generated by Django 4.1.7 on 2023-04-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='sli1.jpg', upload_to='postpics/'),
        ),
    ]