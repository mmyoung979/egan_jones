# Generated by Django 3.0.1 on 2019-12-19 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flows', '0003_auto_20191219_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statementsofcashflows',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 19, 13, 6, 19, 613508)),
        ),
    ]
