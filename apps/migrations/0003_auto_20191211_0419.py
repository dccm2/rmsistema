# Generated by Django 2.2.8 on 2019-12-11 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20191211_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='id',
            field=models.AutoField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
