# Generated by Django 4.1.2 on 2022-10-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loteria', '0006_apostas_clientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apostas',
            name='clientes',
        ),
        migrations.AddField(
            model_name='apostas',
            name='clientes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loteria.cliente'),
            preserve_default=False,
        ),
    ]
