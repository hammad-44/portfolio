# Generated by Django 4.2.2 on 2023-07-09 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(default=django.utils.timezone.now, max_length=100)),
                ('message', models.TextField(default=django.utils.timezone.now, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
