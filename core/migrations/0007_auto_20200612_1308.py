# Generated by Django 3.0.7 on 2020-06-12 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_auto_20200612_1151'),
        ('core', '0006_pontosturisticus_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontosturisticus',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco'),
        ),
    ]
