# Generated by Django 2.2.6 on 2020-08-29 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20200829_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiztaker',
            name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='option1',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='quiz_taker',
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='QuizTaker',
        ),
    ]