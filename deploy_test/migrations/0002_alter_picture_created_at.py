# Generated by Django 4.0.5 on 2022-06-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Загружено'),
        ),
    ]