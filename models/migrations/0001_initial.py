# Generated by Django 3.0.7 on 2020-06-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
