# Generated by Django 3.2.6 on 2021-08-31 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShowVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bootflash', models.TextField()),
                ('chassis', models.TextField()),
                ('cpu', models.TextField()),
                ('device_name', models.TextField()),
                ('memory', models.TextField()),
                ('model', models.TextField()),
                ('processor_board_id', models.TextField()),
                ('rp', models.TextField()),
                ('slots', models.TextField()),
                ('days', models.TextField()),
                ('hours', models.TextField()),
                ('minutes', models.TextField()),
                ('seconds', models.TextField()),
                ('name', models.TextField()),
                ('os', models.TextField()),
                ('reason', models.TextField()),
                ('system_compile_time', models.TextField()),
                ('system_image_file', models.TextField()),
                ('system_version', models.TextField()),
                ('chassis_sn', models.TextField()),
                ('compiled_by', models.TextField()),
                ('curr_config_register', models.TextField()),
                ('image_id', models.TextField()),
                ('image_type', models.TextField()),
                ('label', models.TextField()),
                ('license_level', models.TextField()),
                ('license_type', models.TextField()),
                ('non_volatile', models.TextField()),
                ('physical', models.TextField()),
                ('next_reload_license_level', models.TextField()),
                ('platform', models.TextField()),
                ('processor_type', models.TextField()),
                ('returned_to_rom_by', models.TextField()),
                ('rom', models.TextField()),
                ('rtr_type', models.TextField()),
                ('uptime', models.TextField()),
                ('uptime_this_cp', models.TextField()),
                ('version_short', models.TextField()),
                ('xe_version', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
