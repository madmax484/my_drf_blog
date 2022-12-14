# Generated by Django 4.1.3 on 2023-01-04 19:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default='2023-01-04'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 1, 4)),
        ),
        migrations.CreateModel(
            name='UserPostRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('is_favorites', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Bad'), (2, 'Not bad'), (3, 'Normal'), (4, 'Good'), (5, 'Very good')])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
