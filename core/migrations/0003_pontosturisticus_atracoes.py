# Generated by Django 3.0.7 on 2020-06-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0002_auto_20200612_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticus',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
