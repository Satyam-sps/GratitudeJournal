# Generated by Django 4.1.3 on 2022-11-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GratitudeJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_entry', models.TextField(help_text="Enter your Today's Journal Entry", max_length=30)),
                ('rate_your_day', models.PositiveSmallIntegerField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Normal'), (2, 'Bad'), (1, 'Very Bad')], default='Good', verbose_name='How is your Day')),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]