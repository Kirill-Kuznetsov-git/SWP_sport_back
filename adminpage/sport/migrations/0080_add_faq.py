# Generated by Django 3.1.8 on 2021-08-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0079_auto_20210816_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'faq category',
                'db_table': 'faq_category',
            },
        ),
        migrations.CreateModel(
            name='FAQElement',
            fields=[
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sport.faqcategory')),
            ],
            options={
                'verbose_name_plural': 'faq element',
                'db_table': 'faq_element',
            },
        ),
    ]