# Generated by Django 3.1.2 on 2020-10-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esi_pricingengine', '0001_initial'),
        ('esi_users', '0002_auto_20201017_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='future',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi_pricingengine.asset'),
        ),
    ]
