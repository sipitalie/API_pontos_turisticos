# Generated by Django 3.0.7 on 2020-06-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontosturisticus_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticus',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
