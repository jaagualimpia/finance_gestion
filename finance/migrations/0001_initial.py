# Generated by Django 4.1.1 on 2023-03-01 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pocket_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('transaction_type', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.user')),
            ],
        ),
        migrations.CreateModel(
            name='PocketTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pocket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.pocket')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='pocket',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.user'),
        ),
    ]
