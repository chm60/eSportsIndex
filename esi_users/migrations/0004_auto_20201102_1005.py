# Generated by Django 3.1.2 on 2020-11-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi_users', '0003_auto_20201018_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=300, null=True),
        ),
    ]