# Generated by Django 4.0.1 on 2022-01-13 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_wight_i_item_weight_i'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price_i',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='weight_i',
            new_name='weight',
        ),
    ]