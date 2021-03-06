# Generated by Django 3.2.6 on 2021-08-23 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_promocional', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('estoque', models.PositiveSmallIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
            options={
                'verbose_name': 'Variação',
                'verbose_name_plural': 'Variações',
            },
        ),
    ]
