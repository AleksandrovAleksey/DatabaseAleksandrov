# Generated by Django 4.2.16 on 2024-11-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_question_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='app.tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
