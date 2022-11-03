# Generated by Django 4.1.2 on 2022-10-27 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0010_cliente_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ganhadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.apostas')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.cliente')),
            ],
        ),
    ]
