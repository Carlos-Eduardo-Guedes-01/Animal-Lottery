# Generated by Django 4.1.2 on 2022-10-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apostas',
            name='clientes',
            field=models.ManyToManyField(blank=True, to='loteria.cliente'),
        ),
    ]