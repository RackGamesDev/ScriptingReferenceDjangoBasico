# Generated by Django 4.2.11 on 2024-10-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_alter_usuario_fecha_publicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='a', max_length=10)),
                ('usuarios', models.ManyToManyField(to='datos.usuario')),
            ],
        ),
    ]
