# Generated by Django 2.1.2 on 2018-10-12 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('leituras', '0015_auto_20181012_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblioteca',
            name='name',
            field=models.CharField(default='name', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livro',
            name='serie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='leituras.Serie'),
        ),
    ]
