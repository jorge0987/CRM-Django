# Generated by Django 4.1.4 on 2022-12-26 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_companyowner_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]