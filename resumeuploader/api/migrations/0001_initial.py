# Generated by Django 5.0.6 on 2024-06-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('West Bengal', 'West Bengal'), ('Bihar', 'Bihar'), ('Jharkhand', 'Jharkhand'), ('Gujarat', 'Gujarat')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdoc', models.FileField(blank=True, upload_to='rdocs')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
