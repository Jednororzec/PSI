# Generated by Django 2.0.13 on 2019-12-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('e_mail', models.CharField(max_length=150)),
                ('miasto', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=50)),
            ],
        ),
    ]
