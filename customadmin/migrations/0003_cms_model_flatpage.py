# Generated by Django 3.2.13 on 2022-04-14 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customadmin', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('enable_comments', models.BooleanField(default=False)),
                ('template_name', models.CharField(blank=True, max_length=70)),
                ('registration_required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CMS_Model',
            fields=[
                ('flatpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customadmin.flatpage')),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_desc', models.TextField(blank=True, null=True)),
                ('meta_key', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CMS_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CMS_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cms',
            },
            bases=('customadmin.flatpage',),
        ),
    ]
