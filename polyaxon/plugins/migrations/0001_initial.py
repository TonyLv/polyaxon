# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 15:30
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import libs.spec_validation
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotebookJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, help_text='The yaml content of the plugin polyaxonfile/specification.', null=True, validators=[libs.spec_validation.validate_tensorboard_spec_content])),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(help_text='The compiled polyaxonfile for tensorboard.', validators=[libs.spec_validation.validate_tensorboard_spec_content])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotebookJobStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(blank=True, choices=[('Created', 'Created'), ('Building', 'Building'), ('Running', 'Running'), ('Succeeded', 'Succeeded'), ('Failed', 'Failed'), ('Deleted', 'Deleted'), ('UNKNOWN', 'UNKNOWN')], default='Created', max_length=64, null=True)),
                ('message', models.CharField(blank=True, max_length=256, null=True)),
                ('details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='plugins.NotebookJob')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
                'verbose_name_plural': 'Notebook Job Statuses',
            },
        ),
        migrations.CreateModel(
            name='TensorboardJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True, help_text='The yaml content of the plugin polyaxonfile/specification.', null=True, validators=[libs.spec_validation.validate_tensorboard_spec_content])),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(help_text='The compiled polyaxonfile for tensorboard.', validators=[libs.spec_validation.validate_tensorboard_spec_content])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TensorboardJobStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('status', models.CharField(blank=True, choices=[('Created', 'Created'), ('Building', 'Building'), ('Running', 'Running'), ('Succeeded', 'Succeeded'), ('Failed', 'Failed'), ('Deleted', 'Deleted'), ('UNKNOWN', 'UNKNOWN')], default='Created', max_length=64, null=True)),
                ('message', models.CharField(blank=True, max_length=256, null=True)),
                ('details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='plugins.TensorboardJob')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
                'verbose_name_plural': 'Tensorboard Job Statuses',
            },
        ),
        migrations.AddField(
            model_name='tensorboardjob',
            name='job_status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='plugins.TensorboardJobStatus'),
        ),
        migrations.AddField(
            model_name='tensorboardjob',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notebookjob',
            name='job_status',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='plugins.NotebookJobStatus'),
        ),
        migrations.AddField(
            model_name='notebookjob',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
