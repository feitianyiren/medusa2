# Generated by Django 2.0 on 2018-09-21 19:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leituras', '0007_auto_20180913_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leitura_Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('IN', 'Iniciada'), ('LD', 'lida até'), ('FN', 'Finalizada'), ('AB', 'abadonada')], default='IN', max_length=2)),
                ('pagina', models.IntegerField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da atualização')),
            ],
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'ordering': ['autor', 'serie', 'nSerie', 'titulo']},
        ),
        migrations.RemoveField(
            model_name='leitura',
            name='dataDeFim',
        ),
        migrations.RemoveField(
            model_name='leitura',
            name='dataDeInicio',
        ),
        migrations.RemoveField(
            model_name='leitura',
            name='status',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='lido',
        ),
        migrations.AddField(
            model_name='leitura',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data que a leitura foi criada'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leitura',
            name='dataUpdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Data em que a leitura foi atualizada'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leituras.Editora'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='leituras.serie'),
        ),
        migrations.AddField(
            model_name='leitura_update',
            name='leitura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leituras.Leitura'),
        ),
    ]
