# Generated by Django 3.0 on 2019-12-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191213_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnologia',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Responsivo'), ('lni-leaf', 'Design Moderno'), ('lni-layers', 'Modelo Multiuso'), ('lni-user', 'Formulario'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Icone'),
        ),
    ]
