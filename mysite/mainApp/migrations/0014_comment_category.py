# Generated by Django 2.2.6 on 2019-12-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20191219_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Category'),
            preserve_default=False,
        ),
    ]
