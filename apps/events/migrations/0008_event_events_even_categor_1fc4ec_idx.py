# Generated by Django 4.2.5 on 2024-02-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_event_like_event_rating'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['category', 'title', 'venue'], name='events_even_categor_1fc4ec_idx'),
        ),
    ]