# Generated by Django 5.1.2 on 2024-11-11 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'default_permissions': (), 'permissions': (('can_add_book', 'Can add book'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book'))},
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Admin', 'administrator'), ('Librarian', 'librarian'), ('Member', 'member')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
