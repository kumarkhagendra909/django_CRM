# Generated by Django 4.1.2 on 2023-10-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_record_trial_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
