# Generated by Django 4.0.3 on 2022-03-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]