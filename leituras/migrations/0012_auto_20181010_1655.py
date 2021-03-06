# Generated by Django 2.1.2 on 2018-10-10 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('leituras', '0011_auto_20181010_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='lido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='leituras.Serie'),
        ),
    ]
