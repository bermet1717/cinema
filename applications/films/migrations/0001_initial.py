# Generated by Django 4.0.3 on 2022-04-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('slug', models.SlugField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
