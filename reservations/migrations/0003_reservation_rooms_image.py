# Generated by Django 4.0.4 on 2022-04-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_reservation_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rooms_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]