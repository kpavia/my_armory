# Generated by Django 4.0.5 on 2022-06-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firearm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firearm',
            name='type',
            field=models.CharField(choices=[('rifle', 'Rifle'), ('shotgun', 'Shotgun'), ('handgun', 'Handgun'), ('revolver', 'Revolver'), ('musket', 'Musket'), ('mg', 'Machine Gun'), ('smg', 'Submachine Gun')], max_length=8),
        ),
    ]
