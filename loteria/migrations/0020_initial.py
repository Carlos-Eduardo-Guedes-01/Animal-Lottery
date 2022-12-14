# Generated by Django 4.1.2 on 2022-10-28 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loteria', '0019_remove_sorteio_aposta_delete_apostas_delete_sorteio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor1', models.IntegerField()),
                ('valor2', models.IntegerField()),
                ('valor3', models.IntegerField()),
                ('valor4', models.IntegerField()),
                ('valor5', models.IntegerField()),
                ('valor6', models.IntegerField()),
                ('data_aposta', models.DateField()),
                ('valor_aposta', models.FloatField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sorteio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor1', models.IntegerField()),
                ('valor2', models.IntegerField()),
                ('valor3', models.IntegerField()),
                ('valor4', models.IntegerField()),
                ('valor5', models.IntegerField()),
                ('valor6', models.IntegerField()),
                ('data_sorteio', models.DateField(null=True)),
                ('aposta', models.ManyToManyField(null=True, to='loteria.apostas')),
            ],
        ),
    ]
