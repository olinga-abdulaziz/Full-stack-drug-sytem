# Generated by Django 3.2.9 on 2021-11-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=255)),
                ('compony', models.CharField(max_length=255)),
            ],
        ),
    ]
