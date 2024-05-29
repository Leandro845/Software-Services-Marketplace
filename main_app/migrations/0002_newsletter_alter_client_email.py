# Generated by Django 5.0.4 on 2024-05-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=60),
        ),
    ]
