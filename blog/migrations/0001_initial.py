# Generated by Django 2.2.10 on 2020-02-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('entry', models.TextField()),
                ('visible', models.BooleanField(default=False)),
                ('publish_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]