# Generated by Django 2.2.7 on 2019-12-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_edit_projects_form_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalresource',
            name='listing_order',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='resource',
            name='listing_order',
            field=models.IntegerField(default='0'),
        ),
    ]
