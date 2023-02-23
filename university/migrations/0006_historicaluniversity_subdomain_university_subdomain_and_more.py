# Generated by Django 4.1.2 on 2022-12-02 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_historicaluniversity_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluniversity',
            name='subdomain',
            field=models.CharField(default='Set Subdomain of tenant, i.e. unomaha', max_length=255),
        ),
        migrations.AddField(
            model_name='university',
            name='subdomain',
            field=models.CharField(default='Set Subdomain of tenant, i.e. unomaha', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicaluniversity',
            name='primary_color',
            field=models.CharField(default='#000000', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicaluniversity',
            name='secondary_color',
            field=models.CharField(default='#000000', max_length=255),
        ),
        migrations.AlterField(
            model_name='university',
            name='primary_color',
            field=models.CharField(default='#000000', max_length=255),
        ),
        migrations.AlterField(
            model_name='university',
            name='secondary_color',
            field=models.CharField(default='#000000', max_length=255),
        ),
    ]