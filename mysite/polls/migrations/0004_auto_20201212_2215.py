# Generated by Django 2.2.17 on 2020-12-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20201209_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='a_choice_text',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='b_choice_text',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='c_choice_text',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='d_choice_text',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]
