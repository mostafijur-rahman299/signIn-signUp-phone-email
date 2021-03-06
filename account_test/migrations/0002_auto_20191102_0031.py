# Generated by Django 2.2.6 on 2019-11-01 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(help_text='i. Keep an unique email.', max_length=255, unique=True),
        ),
    ]
