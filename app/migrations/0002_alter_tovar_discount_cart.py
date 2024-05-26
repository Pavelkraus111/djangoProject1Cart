# Generated by Django 5.0.6 on 2024-05-18 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('summa', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Сумма')),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tovar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
