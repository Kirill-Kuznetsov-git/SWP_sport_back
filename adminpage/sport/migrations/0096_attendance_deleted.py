# Generated by Django 3.1.8 on 2021-12-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0095_auto_20211209_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
