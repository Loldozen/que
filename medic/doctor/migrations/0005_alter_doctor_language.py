# Generated by Django 3.2 on 2021-05-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='language',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
