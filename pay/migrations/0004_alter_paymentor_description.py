# Generated by Django 3.2.6 on 2024-02-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_alter_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
