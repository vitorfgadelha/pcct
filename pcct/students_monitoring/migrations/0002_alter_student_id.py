# Generated by Django 4.2.6 on 2023-10-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
