# Generated by Django 3.0.1 on 2020-01-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('tel', models.CharField(max_length=32, verbose_name='电话')),
                ('belong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='所属企业')),
            ],
            options={
                'verbose_name': '企业用户',
                'verbose_name_plural': '企业用户',
            },
        ),
    ]
