# Generated by Django 3.2.6 on 2021-08-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='اسم')),
                ('last_name', models.CharField(max_length=100, verbose_name='فامیلی')),
                ('email', models.EmailField(max_length=254, verbose_name='رایانامه')),
                ('phone', models.CharField(max_length=15, verbose_name='تلفن')),
                ('message', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Pouya',
        ),
    ]