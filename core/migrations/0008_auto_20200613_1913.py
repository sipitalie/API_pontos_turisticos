# Generated by Django 3.0.7 on 2020-06-13 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('core', '0007_auto_20200612_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontosturisticus',
            name='Comentarios',
        ),
        migrations.AddField(
            model_name='pontosturisticus',
            name='comentarios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.Comentario'),
        ),
        migrations.RemoveField(
            model_name='pontosturisticus',
            name='atracoes',
        ),
        migrations.AddField(
            model_name='pontosturisticus',
            name='atracoes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atracoes.Atracao'),
        ),
    ]