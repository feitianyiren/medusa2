# Generated by Django 2.0 on 2018-04-11 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leituras', '0005_auto_20180408_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='leituras.serie'),
        ),
    ]
