# Generated by Django 4.2.5 on 2023-10-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_remove_servicerequest_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="subject",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
