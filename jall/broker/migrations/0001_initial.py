# Generated by Django 2.1.2 on 2018-10-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('YT', 'YouTube'), ('SF', 'Spotify')], default='YT', max_length=2)),
                ('duration', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
