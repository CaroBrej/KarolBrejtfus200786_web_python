# Generated by Django 4.1.5 on 2023-01-16 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysports', '0004_alter_sportclub_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sport_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysports.sportclub'),
        ),
    ]
