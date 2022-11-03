# Generated by Django 4.1.2 on 2022-10-20 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=16)),
                ('logar', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
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
            ],
        ),
        migrations.CreateModel(
            name='Numeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor1', models.IntegerField()),
                ('valor2', models.IntegerField()),
                ('valor3', models.IntegerField()),
                ('valor4', models.IntegerField()),
                ('valor5', models.IntegerField()),
                ('valor6', models.IntegerField()),
                ('data_aposta', models.DateField(null=True)),
                ('clientes', models.ManyToManyField(blank=True, to='loteria.cliente')),
            ],
        ),
    ]
