# Generated by Django 4.2 on 2023-05-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_recordresult_mail_alter_recordresult_symp1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordresult',
            name='is_check',
            field=models.BooleanField(default=True),
        ),
    ]
