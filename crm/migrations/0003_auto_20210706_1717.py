# Generated by Django 3.2.5 on 2021-07-06 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210702_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_name', models.CharField(max_length=200, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Cтатус',
                'verbose_name_plural': 'Cтатусы',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statusname', verbose_name='Статус'),
        ),
    ]
