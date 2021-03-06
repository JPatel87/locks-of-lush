# Generated by Django 3.2 on 2022-05-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('service_type', models.CharField(choices=[('CUT', 'cut'), ('COLOUR', 'colour'), ('STYLE', 'style')], default='CUT', max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
