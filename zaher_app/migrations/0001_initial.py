# Generated by Django 5.1.5 on 2025-01-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_activity', models.TextField(max_length=1000)),
                ('current_activity', models.CharField(max_length=500)),
                ('workforce', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('headquarter_address', models.CharField(max_length=300)),
                ('main_warehouse_address', models.CharField(max_length=300)),
                ('maintenance_center_address', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Company Info',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration_number', models.CharField(max_length=20)),
                ('workshop_number', models.CharField(max_length=20)),
                ('sales_number', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Contact Info',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='service-images/')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
