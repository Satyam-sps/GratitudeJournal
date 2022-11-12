# Generated by Django 4.1.3 on 2022-11-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudejournal', '0012_alter_attachment_grat_attach_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='grat_attach_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gratitudejournal',
            name='rate_your_day',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Very Good'), (4, 'Good'), (3, 'Normal'), (2, 'Bad'), (1, 'Very Bad')], default=5, verbose_name='How is your Day'),
        ),
    ]