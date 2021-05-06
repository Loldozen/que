# Generated by Django 3.2 on 2021-05-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='language',
            field=models.JSONField(verbose_name='Lamguages you can consult with'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=50, verbose_name='Specialization'),
        ),
    ]