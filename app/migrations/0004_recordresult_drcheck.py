# Generated by Django 4.2 on 2023-05-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_recordresult_is_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordresult',
            name='drcheck',
            field=models.BooleanField(default=True),
        ),
    ]
