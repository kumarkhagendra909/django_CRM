# Generated by Django 4.2.6 on 2023-10-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_record_refered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='trial_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]