# Generated by Django 4.0.2 on 2022-03-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_parrafo_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
