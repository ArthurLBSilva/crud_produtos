# Generated by Django 5.1.4 on 2025-01-14 02:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('quantidade_estoque', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
