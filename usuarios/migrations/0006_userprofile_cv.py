# Generated by Django 3.2.9 on 2021-11-09 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0006_alter_cv_licencias'),
        ('usuarios', '0005_rename_usuario_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CV.cv'),
        ),
    ]
