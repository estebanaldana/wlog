# Generated by Django 2.1.7 on 2019-02-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='idContent',
            field=models.CharField(max_length=50, null=True),
        ),
    ]