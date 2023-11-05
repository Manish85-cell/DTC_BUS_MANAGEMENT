# Generated by Django 4.1.7 on 2023-11-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reachable', models.IntegerField(max_length=255)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='routes.busstand')),
            ],
        ),
    ]