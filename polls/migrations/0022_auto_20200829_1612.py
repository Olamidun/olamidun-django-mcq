# Generated by Django 2.2.6 on 2020-08-29 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20200829_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('question1', models.CharField(max_length=200)),
                ('question2', models.CharField(max_length=200)),
                ('question3', models.CharField(max_length=200)),
                ('question4', models.CharField(max_length=200)),
                ('question5', models.CharField(max_length=200)),
                ('question6', models.CharField(max_length=200)),
                ('question7', models.CharField(max_length=200)),
                ('question8', models.CharField(max_length=200)),
                ('question9', models.CharField(max_length=200)),
                ('question10', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
        migrations.AddField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Quiz'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questions'),
        ),
    ]
