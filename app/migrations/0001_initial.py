# Generated by Django 4.2 on 2023-04-14 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recordresult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.BigIntegerField(max_length=10)),
                ('mail', models.BigIntegerField(max_length=10)),
                ('symp1', models.BigIntegerField(max_length=10)),
                ('symp2', models.BigIntegerField(max_length=10)),
                ('symp3', models.BigIntegerField(max_length=10)),
                ('symp4', models.BigIntegerField(max_length=10)),
                ('symp5', models.BigIntegerField(max_length=10)),
                ('symp6', models.BigIntegerField(max_length=10)),
                ('symp7', models.BigIntegerField(max_length=10)),
                ('symp8', models.BigIntegerField(max_length=10)),
                ('Image', models.ImageField(upload_to='image/')),
                ('Predicteddegree', models.CharField(max_length=50)),
                ('Dateandtime', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]