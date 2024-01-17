# Generated by Django 4.1.13 on 2024-01-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Did', models.IntegerField()),
                ('Dname', models.CharField(max_length=25)),
                ('prec', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'Disease',
            },
        ),
    ]
