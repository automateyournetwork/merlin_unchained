# Generated by Django 3.2.6 on 2021-09-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0002_showipintbrief'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyats_alias', models.TextField()),
                ('os', models.TextField()),
                ('part', models.TextField()),
                ('description', models.TextField()),
                ('pid', models.TextField()),
                ('serial_number', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]