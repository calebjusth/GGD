# Generated by Django 4.0 on 2023-11-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('address', models.TextField()),
            ],
        ),
    ]
