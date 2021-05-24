# Generated by Django 3.2.2 on 2021-05-19 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210516_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='films',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterField(
            model_name='films',
            name='file_image',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('raiting', models.CharField(max_length=5)),
                ('date_release', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=10)),
                ('file_image', models.ImageField(upload_to='img/')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.genres')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
    ]