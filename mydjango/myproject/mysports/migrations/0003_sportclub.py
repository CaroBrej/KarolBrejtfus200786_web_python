# Generated by Django 4.1.5 on 2023-01-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysports', '0002_alter_person_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportClub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]