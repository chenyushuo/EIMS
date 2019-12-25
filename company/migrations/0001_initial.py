# Generated by Django 3.0.1 on 2019-12-24 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniform_social_credit_code', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=128)),
                ('registered_capital', models.CharField(max_length=64)),
                ('paid_up_capital', models.CharField(max_length=64)),
                ('business_scope', models.CharField(max_length=1024)),
                ('industry', models.CharField(max_length=128)),
                ('tel', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('province', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('district', models.CharField(max_length=32)),
                ('detail_address', models.CharField(max_length=128)),
                ('company_type', models.CharField(max_length=128)),
                ('business_registration_number', models.CharField(max_length=14)),
                ('registration_authority', models.CharField(max_length=128)),
                ('operating_status', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('image_url', models.URLField()),
                ('name', models.CharField(max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=64)),
                ('process', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=16)),
                ('trademark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Trademark')),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateField()),
                ('change_item', models.CharField(max_length=64)),
                ('before_change', models.CharField(max_length=1024)),
                ('after_change', models.CharField(max_length=1024)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]