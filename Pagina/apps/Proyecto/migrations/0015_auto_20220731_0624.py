# Generated by Django 2.0.3 on 2022-07-31 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0014_auto_20220731_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_producto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
