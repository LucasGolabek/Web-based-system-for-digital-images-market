# Generated by Django 4.0.4 on 2022-11-20 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_messages_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='negotiation_status',
            field=models.CharField(choices=[('A', 'Zaakceptowana'), ('O', 'Odrzucona'), ('C', 'Oczekująca')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='messages',
            name='photo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]