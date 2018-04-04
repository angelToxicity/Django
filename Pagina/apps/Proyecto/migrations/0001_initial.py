# Generated by Django 2.0.3 on 2018-03-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=150)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('fecha_publicacion', models.DateField()),
                ('votos', models.IntegerField()),
            ],
        ),
    ]
