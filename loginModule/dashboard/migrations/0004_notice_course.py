# Generated by Django 4.0 on 2022-01-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='course',
            field=models.ManyToManyField(related_name='notice', to='dashboard.Course'),
        ),
    ]
