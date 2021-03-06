# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default=None, max_length=256, verbose_name='Problem Question')),
                ('answerChoice1', models.CharField(default=None, max_length=100, verbose_name='Answer Choice 1')),
                ('answerChoice2', models.CharField(default=None, max_length=100, verbose_name='Answer Choice 2')),
                ('answerChoice3', models.CharField(default=None, max_length=100, verbose_name='Answer Choice 3')),
                ('answerChoice4', models.CharField(default=None, max_length=100, verbose_name='Answer Choice 4')),
                ('correctAnswer', models.IntegerField(default=None, verbose_name='Correct Answer')),
                ('illustration', models.ImageField(blank=True, null=True, upload_to='illustrations/')),
            ],
            options={
                'verbose_name_plural': 'Problem Questions',
            },
        ),
        migrations.CreateModel(
            name='QuizAgeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minAgeLevel', models.IntegerField(verbose_name='Minimum Age Level')),
                ('maxAgeLevel', models.IntegerField(verbose_name='Maximum Age Level')),
            ],
            options={
                'verbose_name_plural': 'Problem Questions Age Groups',
            },
        ),
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Quiz Categories',
            },
        ),
        migrations.CreateModel(
            name='QuizInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=24, verbose_name='User identifier')),
                ('userSession', models.CharField(max_length=24, verbose_name='Unique user session identifier')),
                ('userAnswer', models.IntegerField(verbose_name='User answer')),
                ('userCorrectorNot', models.BooleanField(verbose_name='User got the right answer?')),
                ('quizDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('problemQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.ProblemQuestion')),
            ],
            options={
                'verbose_name_plural': 'Quiz Instances',
            },
        ),
        migrations.AddField(
            model_name='problemquestion',
            name='ageGroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.QuizAgeGroup'),
        ),
        migrations.AddField(
            model_name='problemquestion',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.QuizCategory'),
        ),
    ]
