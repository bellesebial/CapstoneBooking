# Generated by Django 3.2 on 2023-05-20 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0003_auto_20230520_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='endTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='startTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='BookingAttendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendee', to='BookingApp.user')),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BookingApp.booking')),
            ],
        ),
    ]
