# Generated by Django 4.1.4 on 2022-12-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de Edicion')),
            ],
            options={
                'verbose_name': 'pagina',
                'verbose_name_plural': 'paginas',
                'ordering': ['title'],
            },
        ),
    ]
