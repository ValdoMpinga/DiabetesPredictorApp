# Generated by Django 4.0.6 on 2022-07-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_TrainerCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('re_trainNumber', models.IntegerField(default=500)),
            ],
        ),
    ]
