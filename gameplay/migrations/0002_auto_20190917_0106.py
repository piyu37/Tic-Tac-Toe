# Generated by Django 2.2.5 on 2019-09-17 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('W', 'First Player Wins'), ('S', 'Second Player To Move'), ('D', 'Draw'), ('F', 'First Player To Move'), ('L', 'Second Player Wins')], default='F', max_length=1),
        ),
    ]