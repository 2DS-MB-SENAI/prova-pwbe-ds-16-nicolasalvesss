# Generated by Django 4.2 on 2025-04-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_alter_medico_crm_alter_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
