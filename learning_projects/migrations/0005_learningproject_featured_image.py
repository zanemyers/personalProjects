# Generated by Django 4.1.7 on 2023-03-31 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_projects', '0004_tag_learningproject_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningproject',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
