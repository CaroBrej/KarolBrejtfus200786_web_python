# Generated by Django 4.1.5 on 2023-01-17 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysports', '0006_person_born_year_person_role_turnament_results'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Turnament',
            new_name='Tournament',
        ),
        migrations.RenameField(
            model_name='results',
            old_name='turnament',
            new_name='tournament',
        ),
    ]
