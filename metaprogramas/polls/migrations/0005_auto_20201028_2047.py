# Generated by Django 3.1.2 on 2020-10-29 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201028_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polls',
            name='answer_boolean',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='candidate_email',
        ),
        migrations.AddField(
            model_name='polls',
            name='answer_id',
            field=models.ManyToManyField(to='polls.Answers'),
        ),
        migrations.AddField(
            model_name='polls',
            name='candidate_id',
            field=models.ManyToManyField(to='polls.Candidates'),
        ),
        migrations.RemoveField(
            model_name='answers',
            name='answer_boolean',
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_boolean',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='answers',
            name='answer_text',
        ),
        migrations.AddField(
            model_name='answers',
            name='answer_text',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='candidates',
            name='email',
        ),
        migrations.AddField(
            model_name='candidates',
            name='email',
            field=models.EmailField(default='noreply@noreply.com', max_length=254),
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question_text',
        ),
        migrations.AddField(
            model_name='polls',
            name='question_text',
            field=models.ManyToManyField(to='polls.Questions'),
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question_text',
        ),
        migrations.AddField(
            model_name='questions',
            name='question_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]