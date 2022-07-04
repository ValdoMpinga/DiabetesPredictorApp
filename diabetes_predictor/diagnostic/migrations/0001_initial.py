# Generated by Django 4.0.5 on 2022-07-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosticResult', models.IntegerField()),
                ('diagnosticProbability', models.IntegerField()),
                ('diagnosticDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.TextField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='Feminino')),
                ('peso', models.CharField(max_length=10)),
                ('altura', models.CharField(max_length=10)),
                ('glicemia', models.CharField(max_length=10)),
                ('data', models.DateField()),
            ],
        ),
    ]