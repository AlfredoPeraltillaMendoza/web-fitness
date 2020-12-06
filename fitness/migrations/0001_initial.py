# Generated by Django 2.1.5 on 2020-12-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('peso', models.IntegerField()),
                ('talla', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fechaInicio', models.DateTimeField(auto_now_add=True)),
                ('fechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]