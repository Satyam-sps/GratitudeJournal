# Generated by Django 4.1.3 on 2022-11-10 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gratitudejournal', '0009_gratitudejournal_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifelog_detail', models.TextField()),
                ('date_created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_detail', models.TextField()),
                ('date_created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='attachment',
            old_name='gratitude_attach',
            new_name='gratitude_attach_key',
        ),
        migrations.AddField(
            model_name='attachment',
            name='grat_attach_img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='life_log_attach_img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='prescrip_attach_img',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='gratitudejournal',
            name='journal_entry',
            field=models.TextField(help_text="Enter your Today's Journal Entry"),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='life_log_attach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='life_log_attach', to='gratitudejournal.lifelog'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='prescription_attach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_attach', to='gratitudejournal.prescription'),
        ),
    ]
