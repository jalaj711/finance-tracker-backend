# Generated by Django 4.1.3 on 2022-12-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0, verbose_name='Transaction Amount'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(default=0, verbose_name='Current Balance'),
        ),
    ]
