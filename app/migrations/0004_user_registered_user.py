# Generated by Django 5.0.2 on 2024-06-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_email_alter_user_personal_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='registered_user',
            field=models.BooleanField(default=True),
        ),
    ]