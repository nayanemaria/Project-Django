# Generated by Django 4.0.6 on 2022-08-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_aluno_escola_alter_aluno_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escola',
            name='escola',
        ),
        migrations.AddField(
            model_name='escola',
            name='nome',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='nome'),
        ),
    ]
