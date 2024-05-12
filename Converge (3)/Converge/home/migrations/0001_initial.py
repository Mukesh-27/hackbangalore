# Generated by Django 5.0.6 on 2024-05-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('project_title', models.CharField(max_length=255)),
                ('project_description', models.TextField()),
                ('file', models.FileField(upload_to='files/')),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=25)),
                ('confpassword', models.CharField(max_length=255)),
                ('Contactnumber', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=355)),
            ],
        ),
    ]
