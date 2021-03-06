# Generated by Django 2.0.2 on 2019-01-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='introduction',
            new_name='intro',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_link',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_icon',
        ),
        migrations.AddField(
            model_name='product',
            name='icon',
            field=models.ImageField(default='default_icon.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.png', upload_to='images/'),
        ),
    ]
