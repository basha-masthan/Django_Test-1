# Generated by Django 5.0.6 on 2024-08-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0006_remove_cart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usrdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='usrdata',
            name='email',
            field=models.EmailField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]