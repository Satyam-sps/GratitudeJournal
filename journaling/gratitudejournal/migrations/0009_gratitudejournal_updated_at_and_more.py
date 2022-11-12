# Generated by Django 4.1.3 on 2022-11-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudejournal', '0008_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='gratitudejournal',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gratitudejournal',
            name='journal_entry',
            field=models.TextField(default='{}', help_text="Enter your Today's Journal Entry"),
        ),
    ]