# Generated by Django 3.1.2 on 2020-10-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campeon', models.CharField(max_length=20)),
                ('Duracion', models.DateTimeField()),
                ('kills', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('assist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invocador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=30)),
                ('Nivel', models.IntegerField()),
                ('ChampMain', models.CharField(max_length=30)),
            ],
        ),
    ]
