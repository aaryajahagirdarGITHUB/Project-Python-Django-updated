# Generated by Django 3.1 on 2020-10-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VTAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imge', models.ImageField(upload_to='webimg/aboutImg')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VTPortfolioIot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=200)),
                ('pname', models.CharField(max_length=200)),
                ('imge', models.ImageField(upload_to='webimg/portFolioIotImg')),
            ],
        ),
        migrations.CreateModel(
            name='VTPortfolioMob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=200)),
                ('pname', models.CharField(max_length=200)),
                ('imge', models.ImageField(upload_to='webimg/portFolioMobImg')),
            ],
        ),
        migrations.CreateModel(
            name='VTPortfolioWeb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=200)),
                ('pname', models.CharField(max_length=200)),
                ('imge', models.ImageField(upload_to='webimg/portFolioWebImg')),
            ],
        ),
        migrations.CreateModel(
            name='VTServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imge', models.ImageField(upload_to='webimg/servicesImg')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
            ],
        ),
    ]
