# Generated by Django 4.1.5 on 2023-01-09 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email_addres', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='ClieteModel',
        ),
    ]
