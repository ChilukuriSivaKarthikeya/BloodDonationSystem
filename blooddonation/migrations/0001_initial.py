# Generated by Django 3.2.12 on 2022-09-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bloodgroup', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=12)),
                ('village', models.CharField(max_length=30)),
                ('mandal', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]