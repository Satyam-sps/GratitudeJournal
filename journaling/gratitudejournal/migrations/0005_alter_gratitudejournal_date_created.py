# Generated by Django 4.1.3 on 2022-11-09 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudejournal', '0004_alter_gratitudejournal_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gratitudejournal',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]