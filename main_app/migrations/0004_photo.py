# Generated by Django 3.1.7 on 2021-02-22 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210220_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('icecream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.icecream')),
            ],
        ),
    ]
