# Generated by Django 3.0 on 2019-12-14 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191213_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Responsivo'), ('lni-leaf', 'Design Moderno'), ('lni-layers', 'Modelo Multiuso'), ('lni-user', 'Formulario')], max_length=16, verbose_name='Icone'),
        ),
    ]
