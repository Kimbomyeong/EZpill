# Generated by Django 4.2.7 on 2023-11-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_firebase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='student',
            name='firebase_uid',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]
