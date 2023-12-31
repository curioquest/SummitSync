# Generated by Django 4.2.1 on 2023-05-16 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("presentations", "0002_alter_presentation_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="presentation",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="presentations",
                to="presentations.status",
            ),
        ),
    ]
