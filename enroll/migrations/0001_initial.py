# Generated by Django 3.2.3 on 2021-06-16 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('problem', models.TextField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=60)),
                ('urls', models.URLField()),
                ('headquarter', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Typeofpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gallerypost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(default='', upload_to='gallery', verbose_name='Image_view')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.district')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.typeofpost')),
            ],
        ),
        migrations.CreateModel(
            name='Allpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(default='', upload_to='allpost', verbose_name='Image_view')),
                ('dec', models.TextField(max_length=2000)),
                ('how_to_reach', models.FileField(default='', upload_to='how_to_reach', verbose_name='Image_view1')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.district')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.typeofpost')),
            ],
        ),
    ]