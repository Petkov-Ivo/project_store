# Generated by Django 3.1.1 on 2020-12-05 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customer',
            new_name='user',
        ),
    ]
