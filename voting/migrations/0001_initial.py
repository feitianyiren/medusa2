# Generated by Django 2.0 on 2018-09-30 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandato', models.DurationField()),
                ('nome', models.CharField(max_length=100)),
                ('tem_voto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CasaVotante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('autoridade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('quorumMinimo', models.DecimalField(decimal_places=2, max_digits=3)),
                ('porcentagemDaCasa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('texto', models.TextField()),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.CasaVotante')),
            ],
        ),
        migrations.CreateModel(
            name='PosVoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoMocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(max_length=20)),
                ('quorumMinimo', models.DecimalField(decimal_places=2, max_digits=3)),
                ('porcentagemDaCasa', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podeAbster', models.BooleanField()),
                ('casa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.CasaVotante')),
                ('mocoes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.Mocao')),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assinatura', models.CharField(max_length=40)),
                ('cadeira', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.Cadeira')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.Votacao')),
                ('voto',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='voting.PosVoto')),
            ],
        ),
        migrations.AddField(
            model_name='posvoto',
            name='votacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Votacao'),
        ),
        migrations.AddField(
            model_name='mocao',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.TipoMocao'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='casa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.CasaVotante'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='voting.Cargo'),
        ),
        migrations.AddField(
            model_name='cadeira',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
