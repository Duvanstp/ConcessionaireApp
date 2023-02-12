# Generated by Django 4.1.4 on 2023-02-12 00:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('mileage', models.FloatField()),
                ('price', models.FloatField()),
                ('model', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=50)),
                ('id_vehicle', models.CharField(max_length=50)),
                ('in_promotion', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('owners', models.CharField(default='', max_length=50)),
                ('main_view', models.ImageField(upload_to='automobile/')),
                ('front_view', models.ImageField(upload_to='automobile/')),
                ('back_view', models.ImageField(upload_to='automobile/')),
                ('profile_view', models.ImageField(upload_to='automobile/')),
                ('engine_view', models.ImageField(upload_to='automobile/')),
                ('dashboard_view', models.ImageField(upload_to='automobile/')),
                ('gallery', models.ImageField(upload_to='automobile/')),
                ('exterior_color', models.CharField(max_length=50)),
                ('interior_color', models.CharField(max_length=50)),
                ('VIN', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(default=5)),
                ('engine_size', models.CharField(max_length=50)),
                ('accidents', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
                ('body_shape', models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Cabriolet', 'Cabriolet'), ('Pickup', 'Pickup'), ('Wagon', 'Wagon'), ('Van', 'Van'), ('SUV', 'SUV')], default='Sedan', max_length=50)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Auto', 'Auto')], default='Manual', max_length=20)),
                ('title_status', models.CharField(choices=[('Clean', 'Clean'), ('Rebuild/Reconstructed', 'Rebuild/Reconstructed')], default='Clean', max_length=50)),
                ('traction', models.CharField(choices=[('4WD', '4WD'), ('AWD', 'AWD'), ('FWD', 'FWD'), ('RWD', 'RWD')], default='4WD', max_length=50)),
                ('fuel', models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], default='Gasoline', max_length=20)),
                ('seats_materials', models.CharField(choices=[('Leather', 'Leather'), ('Cloth', 'Cloth')], default='Leather', max_length=20)),
                ('electric_parking_brake', models.BooleanField(default=False)),
                ('power_seats', models.BooleanField(default=False)),
                ('reverse_camera', models.BooleanField(default=False)),
                ('reversing_sensors', models.BooleanField(default=False)),
                ('navigation_system', models.BooleanField(default=False)),
                ('moonroof', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('automobile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concessionaire.automobile')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concessionaire.business')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('seccion_1', models.TextField()),
                ('seccion_2', models.TextField()),
                ('seccion_3', models.TextField()),
                ('img_main', models.ImageField(upload_to='')),
                ('img_seccion_1', models.ImageField(upload_to='post/')),
                ('img_seccion_2', models.ImageField(upload_to='post/')),
                ('img_seccion_3', models.ImageField(upload_to='post/')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durations', models.TimeField()),
                ('new_price', models.FloatField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concessionaire.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_employee', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=20)),
                ('token', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('business', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='concessionaire.business')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
