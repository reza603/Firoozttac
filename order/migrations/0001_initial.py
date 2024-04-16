# Generated by Django 4.2.1 on 2023-07-10 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_addr', models.FileField(upload_to='XmlFiles/%Y/%m/%d/', verbose_name='انتخاب فایل')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tblXmlOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oc', models.CharField(max_length=11)),
                ('lc', models.CharField(max_length=11)),
                ('no', models.PositiveIntegerField()),
                ('px', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='dis', max_length=3)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.document')),
            ],
        ),
        migrations.CreateModel(
            name='tblOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bn', models.CharField(max_length=14)),
                ('md', models.CharField(max_length=10)),
                ('ed', models.CharField(max_length=10)),
                ('no', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='dis', max_length=3, verbose_name=(('en', 'قابل استعلام'), ('dis', 'غیرقابل استعلام')))),
                ('GTIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('invoicenumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.tblxmlorders')),
            ],
        ),
    ]
