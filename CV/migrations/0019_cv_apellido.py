# Generated by Django 3.2.8 on 2021-11-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0018_alter_cv_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='apellido',
            field=models.CharField(max_length=50, null=True),
        ),
    ]