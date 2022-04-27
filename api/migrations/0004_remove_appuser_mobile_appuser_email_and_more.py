# Generated by Django 4.0.4 on 2022-04-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='mobile',
        ),
        migrations.AddField(
            model_name='appuser',
            name='email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]