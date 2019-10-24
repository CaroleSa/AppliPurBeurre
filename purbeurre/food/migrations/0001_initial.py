# Generated by Django 2.2.6 on 2019-10-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('url_picture', models.URLField(unique=True)),
                ('link', models.URLField(unique=True)),
                ('energy', models.CharField(max_length=10, null=True)),
                ('proteins', models.CharField(max_length=10, null=True)),
                ('fat', models.CharField(max_length=10, null=True)),
                ('carbohydrates', models.CharField(max_length=10, null=True)),
                ('sugars', models.CharField(max_length=10, null=True)),
                ('fiber', models.CharField(max_length=10, null=True)),
                ('sodium', models.CharField(max_length=10, null=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Food')),
            ],
        ),
    ]
