# Generated by Django 5.0.7 on 2024-11-11 12:20

import django.db.models.deletion
import tickets.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=tickets.models.upload_attachment)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_attachments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('cat', models.PositiveSmallIntegerField(choices=[(2, 'Technical Dept.'), (1, 'Sale Dept.')])),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Urgent'), (2, 'High'), (3, 'Moderate'), (4, 'Low')])),
                ('subject', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Open'), (1, 'Closed')], default=0)),
                ('accountable', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL)),
                ('attachments', models.ManyToManyField(to='tickets.attachment')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('attachments', models.ManyToManyField(to='tickets.attachment')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='followups', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='followups', to='tickets.ticket')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
