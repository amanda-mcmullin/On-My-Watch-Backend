# Generated by Django 4.0.6 on 2022-08-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0008_recommendation_emotion_alter_recommendation_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tags',
            field=models.CharField(max_length=50),
        ),
    ]