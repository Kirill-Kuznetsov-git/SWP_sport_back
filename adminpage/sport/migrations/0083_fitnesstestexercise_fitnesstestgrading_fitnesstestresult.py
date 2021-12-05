# Generated by Django 3.1.8 on 2021-12-05 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0082_auto_20211205_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessTestExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=50)),
                ('value_unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.fitnesstestexercise')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.student')),
            ],
        ),
        migrations.CreateModel(
            name='FitnessTestGrading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('start_range', models.IntegerField()),
                ('end_range', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.fitnesstestexercise')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.semester')),
            ],
        ),
    ]