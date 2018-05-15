from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtail_embed_videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='embedvideo',
            name='collection',
            field=models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection'),
        ),
    ]
