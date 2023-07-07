# Generated by Django 3.2 on 2023-07-07 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LisenseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=14, validators=[myapp.models.validate_cnic])),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(max_length=255)),
                ('lisense_number', models.CharField(max_length=8)),
                ('height', models.CharField(max_length=5)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10, null=True)),
                ('city', models.CharField(blank=True, choices=[('lahore', 'lahore'), ('Karachi', 'Karachi'), ('Faislbad', 'Faislbad')], max_length=30, null=True)),
                ('vehicle_type', models.CharField(choices=[('motor_cycle', 'motor_cycle'), ('car', 'car'), ('jeep', 'jeep'), ('mazda', 'mazda'), ('truck', 'truck')], max_length=20)),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='image/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
