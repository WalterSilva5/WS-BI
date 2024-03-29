# Generated by Django 3.1.6 on 2021-03-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda_por_dia_por_vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='data')),
                ('valor', models.FloatField(verbose_name='valor')),
                ('vendedor_idvendedor', models.IntegerField(verbose_name='vendedor_idvendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='nome')),
                ('email', models.CharField(blank='true', max_length=250, verbose_name='email')),
                ('codigo', models.IntegerField(verbose_name='codigo')),
            ],
        ),
    ]
