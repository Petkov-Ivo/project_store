# Generated by Django 3.1.1 on 2020-12-05 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_profile_picture'),
        ('store', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
            preserve_default=False,
        ),
    ]
