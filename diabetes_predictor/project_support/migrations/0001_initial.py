# Generated by Django 4.0.5 on 2022-06-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.TextField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='Feminino')),
                ('peso', models.CharField(max_length=10)),
                ('altura', models.CharField(max_length=10)),
                ('glicemia', models.CharField(max_length=10)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DiabetesSamples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField()),
                ('age1', models.IntegerField()),
                ('age2', models.IntegerField()),
                ('age3', models.IntegerField()),
                ('age4', models.IntegerField()),
                ('waist1', models.IntegerField()),
                ('waist2', models.IntegerField()),
                ('waist3', models.IntegerField()),
                ('waist4', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.CharField(max_length=5)),
                ('imc', models.IntegerField()),
                ('physicalExercise', models.IntegerField()),
                ('hypertensionPills', models.IntegerField()),
                ('fruitsAndVegetables1', models.IntegerField()),
                ('fruitsAndVegetables2', models.IntegerField()),
                ('fruitsAndVegetables3', models.IntegerField()),
                ('diabeticFamily1', models.IntegerField()),
                ('diabeticFamily2', models.IntegerField()),
                ('diabeticFamily3', models.IntegerField()),
                ('diabeticFamily4', models.IntegerField()),
                ('eatsAlotFats', models.IntegerField()),
                ('smoke1', models.IntegerField()),
                ('smoke2', models.IntegerField()),
                ('smoke3', models.IntegerField()),
                ('smoke4', models.IntegerField()),
                ('highBloodGlucose1', models.IntegerField()),
                ('highBloodGlucose2', models.IntegerField()),
                ('highBloodGlucose3', models.IntegerField()),
                ('glucoseAnalysis1', models.IntegerField()),
                ('glucoseAnalysis2', models.IntegerField()),
                ('glucoseLevelChange1', models.IntegerField()),
                ('glucoseLevelChange2', models.IntegerField()),
                ('glucoseLevelChange3', models.IntegerField()),
                ('womanGlucoseChange1', models.IntegerField()),
                ('womanGlucoseChange2', models.IntegerField()),
                ('womanGlucoseChange3', models.IntegerField()),
                ('womanGlucoseChange4', models.IntegerField()),
                ('areYouDiabetic', models.IntegerField()),
            ],
        ),
    ]
