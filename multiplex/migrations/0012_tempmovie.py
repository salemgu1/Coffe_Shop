# Generated by Django 3.0.5 on 2020-10-11 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiplex', '0011_distributor_producer_theatre'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('actor', models.CharField(max_length=50, null=True)),
                ('director', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='coffee_pic/coffee_poster/')),
                ('video', models.CharField(max_length=200, null=True)),
                ('release_date', models.DateField()),
                ('out_date', models.DateField()),
                ('producer_price', models.PositiveIntegerField()),
                ('producer_status', models.CharField(choices=[('Not Sold', 'Not Sold'), ('Sold', 'Sold'), ('Pending', 'Pending'), ('Declined', 'Declined')], default='Not Sold', max_length=50)),
                ('distributor_price', models.PositiveIntegerField(null=True)),
                ('distributor_status', models.CharField(choices=[('Not Sold', 'Not Sold'), ('Sold', 'Sold'), ('Pending', 'Pending'), ('Declined', 'Declined')], default='Not Sold', max_length=50)),
                ('distributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='multiplex.Distributor')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multiplex.Producer')),
            ],
        ),
    ]
