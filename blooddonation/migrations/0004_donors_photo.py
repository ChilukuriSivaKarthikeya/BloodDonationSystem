# Generated by Django 3.2.12 on 2022-11-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonation', '0003_alter_donors_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='donors',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
