# Generated by Django 3.1.8 on 2021-08-01 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0062_group_trainers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name': 'teacher', 'verbose_name_plural': 'teachers'},
        ),
        migrations.AddField(
            model_name='semester',
            name='academic_leave_students',
            field=models.ManyToManyField(to='sport.Student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sport.trainer', verbose_name='teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='trainers',
            field=models.ManyToManyField(blank=True, related_name='m2m', to='sport.Trainer', verbose_name='teachers'),
        ),
    ]