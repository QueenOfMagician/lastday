# Generated by Django 4.1.7 on 2023-08-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_users_gender_alter_users_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="gender",
            field=models.CharField(
                choices=[("MAN", "MAN"), ("WOMAN", "WOMAN")], max_length=6
            ),
        ),
    ]
