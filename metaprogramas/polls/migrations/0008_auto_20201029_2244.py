# Generated by Django 3.1.2 on 2020-10-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20201029_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Respuesta', 'verbose_name_plural': 'Respuestas'},
        ),
        migrations.AlterField(
            model_name='polls',
            name='answers_id',
            field=models.ManyToManyField(null=True, to='polls.Answers'),
        ),
        migrations.AlterField(
            model_name='polls',
            name='candidate',
            field=models.ManyToManyField(null=True, to='polls.Candidates'),
        ),
        migrations.AlterField(
            model_name='polls',
            name='creator',
            field=models.CharField(default='Admin', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='email_creator',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='polls',
            name='question_id',
            field=models.ManyToManyField(null=True, to='polls.Questions'),
        ),
    ]
