# Generated by Django 5.0.4 on 2024-05-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets', '0004_expensemanagementmaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRevenueMaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('organization_name', models.CharField(max_length=70)),
                ('group_size', models.IntegerField()),
                ('revenue_goal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_name_second', models.CharField(max_length=70)),
                ('contact_email_second', models.EmailField(max_length=70)),
                ('contact_phone_second', models.CharField(max_length=20)),
                ('additional_notes_second', models.TextField(max_length=1200)),
            ],
        ),
        migrations.AlterField(
            model_name='expensemanagementmaker',
            name='number_of_employees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='softweremaker',
            name='project_duration',
            field=models.IntegerField(),
        ),
    ]