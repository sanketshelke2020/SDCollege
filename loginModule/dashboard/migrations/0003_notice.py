# Generated by Django 4.0 on 2022-01-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_userextended_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('description', models.CharField(max_length=2048)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]