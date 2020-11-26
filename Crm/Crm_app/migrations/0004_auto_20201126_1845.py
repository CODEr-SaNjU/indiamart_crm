# Generated by Django 3.1.3 on 2020-11-26 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Crm_app', '0003_delete_userreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Visit_status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry_Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enq_source', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ck_account',
            name='Booking_Date',
            field=models.DateField(blank=True, null=True, verbose_name='Booking Date'),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='Visit_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='expected_purchase_Date',
            field=models.DateField(blank=True, null=True, verbose_name='Expected Purchase Date'),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='visit_date',
            field=models.DateField(blank=True, null=True, verbose_name='Visit Date'),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='visited_status',
            field=models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=0),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='enquiry_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Crm_app.enquiry_source'),
        ),
        migrations.AddField(
            model_name='ck_account',
            name='profession',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Crm_app.profession'),
        ),
    ]
