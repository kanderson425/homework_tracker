# Generated by Django 2.1.5 on 2019-03-21 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('usertype', models.CharField(choices=[('Instructor', 'Instructor'), ('Student', 'Student')], max_length=200)),
                ('location', models.CharField(choices=[('ATX', 'Austin'), ('DAL', 'Dallas'), ('LA', 'Los Angeles'), ('ATL', 'Atlanta'), ('BOS', 'Botston'), ('CHI', 'Chicago'), ('DEN', 'Denver'), ('NYC', 'New York City'), ('PROV', 'Providence'), ('SD', 'San Diego'), ('SF', 'San Francisco'), ('SEA', 'Seattle'), ('STM', 'Stamford'), ('DC', 'Washington, D.C.'), ('LON', 'London')], max_length=200)),
                ('class_start_date', models.CharField(choices=[('Jan', 'Jan - 2019'), ('Feb', 'Feb - 2019'), ('Mar', 'Mar - 2019')], default='Jan-2019', max_length=200)),
                ('class_type', models.CharField(choices=[('SEI', 'Software Engineering Immersive'), ('DSI', 'Data Science Immersive'), ('UX', 'User Experience Immersive')], max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
