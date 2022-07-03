# Generated by Django 4.0.5 on 2022-07-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0003_account_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='history',
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Transaction.account')),
            ],
        ),
    ]
