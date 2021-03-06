# Generated by Django 3.1.5 on 2021-05-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Advisor Name')),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bookingtime', models.DateTimeField(blank=True, null=True)),
                ('bookingid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
