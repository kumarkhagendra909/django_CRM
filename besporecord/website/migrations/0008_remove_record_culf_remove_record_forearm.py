# Generated by Django 4.1.2 on 2023-10-20 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_record_advance_pay_record_balance_record_bicep_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='culf',
        ),
        migrations.RemoveField(
            model_name='record',
            name='forearm',
        ),
    ]
