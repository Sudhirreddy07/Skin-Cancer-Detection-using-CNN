# Generated by Django 4.2 on 2023-05-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_recordresult_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordresult',
            name='is_check',
            field=models.CharField(max_length=50),
        ),
    ]
