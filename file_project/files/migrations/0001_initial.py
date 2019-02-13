# Generated by Django 2.1.1 on 2019-02-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='files')),
                ('location', models.CharField(max_length=500, null=True)),
                ('file_type', models.CharField(max_length=100, null=True)),
                ('size', models.BinaryField(null=True)),
                ('upload_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
