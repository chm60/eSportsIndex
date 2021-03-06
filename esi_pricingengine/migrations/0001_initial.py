# Generated by Django 3.1.2 on 2020-10-18 11:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('esi_players', '0006_auto_20201004_1433'),
        ('esi_users', '0002_auto_20201017_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=100)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi_players.player')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(default=1)),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi_pricingengine.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esi_users.profile')),
            ],
        ),
    ]
