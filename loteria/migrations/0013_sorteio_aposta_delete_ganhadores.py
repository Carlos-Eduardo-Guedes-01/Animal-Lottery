# Generated by Django 4.1.2 on 2022-10-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0012_remove_ganhadores_cliente_ganhadores_sorteio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorteio',
            name='aposta',
            field=models.ManyToManyField(null=True, to='loteria.apostas'),
        ),
        migrations.DeleteModel(
            name='ganhadores',
        ),
    ]