# Generated by Django 5.0.1 on 2024-03-25 19:54
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('eventReadyAPI', '0026_budget_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventgeneralinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
