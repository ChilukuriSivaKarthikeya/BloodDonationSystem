# Generated by Django 3.2.12 on 2022-10-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='email',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donors',
            name='password',
            field=models.CharField(default=10002, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donors',
            name='status',
            field=models.CharField(default='False', max_length=10),
        ),
    ]
