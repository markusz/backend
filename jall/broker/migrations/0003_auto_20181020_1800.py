# Generated by Django 2.1.2 on 2018-10-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0002_auto_20181020_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('YT', 'YouTube'), ('SF', 'Spotify')], default='YT', max_length=2)),
                ('limits', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='token_type',
            field=models.CharField(choices=[('CK', 'Chicken'), ('CT', 'Cat'), ('DG', 'Dog'), ('HS', 'Horse'), ('EL', 'Elephant')], default='CK', max_length=2),
        ),
        migrations.AlterField(
            model_name='token',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]