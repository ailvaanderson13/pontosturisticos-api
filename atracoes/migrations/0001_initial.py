# Generated by Django 3.2.5 on 2021-07-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario', models.TextField()),
                ('idade_min', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Atração',
                'verbose_name_plural': 'Atrações',
            },
        ),
    ]