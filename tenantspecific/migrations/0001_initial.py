# Generated by Django 4.2.7 on 2023-12-06 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CleaningCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('shift_start', models.TimeField()),
                ('shift_end', models.TimeField()),
                ('assigned_rooms', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('room_number', models.CharField(max_length=10)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenantspecific.guest')),
            ],
        ),
        migrations.CreateModel(
            name='RoomServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_details', models.TextField()),
                ('request_time', models.DateTimeField()),
                ('delivery_time', models.DateTimeField(blank=True, null=True)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=6)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenantspecific.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_date', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=50)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenantspecific.reservation')),
            ],
        ),
    ]
