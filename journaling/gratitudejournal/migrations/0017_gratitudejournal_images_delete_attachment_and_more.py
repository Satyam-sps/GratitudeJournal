# Generated by Django 4.1.3 on 2022-11-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudejournal', '0016_lifelogjournal_attachment_lifelog_attach_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gratitudejournal',
            name='images',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Please Choose your images'),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
        migrations.DeleteModel(
            name='LifeLogJournal',
        ),
    ]
