# Generated by Django 3.2.11 on 2022-09-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_sub_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_content',
            field=models.CharField(max_length=200),
        ),
    ]