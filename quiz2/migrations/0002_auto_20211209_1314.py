# Generated by Django 3.2.9 on 2021-12-09 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='technique',
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert'), (5, 'Master')], default=0, max_length=255, verbose_name='Difficulty'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(default='Описание о Квизе'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Quiz Name'),
        ),
    ]
