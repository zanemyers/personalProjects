# Generated by Django 4.1.7 on 2023-03-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningproject',
            name='demo_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='learningproject',
            name='source_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
