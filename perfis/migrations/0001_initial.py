# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=12)),
                ('nome_empresa', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(related_name='convites_recebidos', on_delete=django.db.models.deletion.PROTECT, to='perfis.Perfil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='convite',
            name='solicitante',
            field=models.ForeignKey(related_name='convites_feitos', on_delete=django.db.models.deletion.PROTECT, to='perfis.Perfil'),
            preserve_default=True,
        ),
    ]
