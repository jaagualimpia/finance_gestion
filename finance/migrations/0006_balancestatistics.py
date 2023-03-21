# Generated by Django 4.1.1 on 2023-03-16 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_remove_pockettransaction_pocket_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.user')),
            ],
        ),
    ]