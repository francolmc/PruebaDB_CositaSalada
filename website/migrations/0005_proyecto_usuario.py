from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_etiqueta_proyecto_etiquetas'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to=settings.AUTH_USER_MODEL),
        ),
    ]
