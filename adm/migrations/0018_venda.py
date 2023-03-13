# Generated by Django 4.1.7 on 2023-03-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0017_produto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.produto')),
            ],
        ),
    ]