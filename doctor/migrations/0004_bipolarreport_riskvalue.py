# Generated by Django 2.1.1 on 2020-05-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_bipolarreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='bipolarreport',
            name='riskvalue',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
