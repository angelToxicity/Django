# Generated by Django 2.0.3 on 2022-07-31 01:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Proyecto', '0010_auto_20220731_0122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registroProducto',
            new_name='registro_producto',
        ),
    ]