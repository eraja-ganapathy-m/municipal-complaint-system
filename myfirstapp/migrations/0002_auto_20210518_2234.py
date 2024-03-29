# Generated by Django 3.1.6 on 2021-05-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15)),
                ('complaint_category', models.CharField(max_length=50)),
                ('complaint_description', models.CharField(max_length=10)),
                ('area_of_complaint', models.CharField(max_length=10)),
                ('date_of_complaint', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='phone',
        ),
        migrations.AddField(
            model_name='complaint',
            name='phone_no',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
