# Generated by Django 4.2.6 on 2023-10-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pantone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('tono', models.IntegerField()),
            ],
        ),
    ]