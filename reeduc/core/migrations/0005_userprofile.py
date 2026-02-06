"""Create UserProfile model."""

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    """Migration for UserProfile."""

    dependencies = [
        ("core", "0004_agendamento"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "cargo_es",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("apoio_adm_estagiario", "Apoio Administrativo/Estagiário"),
                            ("assistente_tecnico_direito", "Assistente Técnico – Bacharel em Direito"),
                            ("assistente_tecnico_pedagogo", "Assistente Técnico – Pedagogo(a)"),
                            ("assistente_tecnico_assistente_social", "Assistente Técnico – Assistente Social"),
                            ("assistente_tecnico_psicologo", "Assistente Técnico – Psicólogo(a)"),
                            ("tj_apoio_adm_estagiario", "TJ - Apoio Administrativo/Estagiário"),
                            ("tj_assistente_tecnico_assistente_social", "TJ - Assistente Técnico – Assistente Social"),
                            ("tj_assistente_tecnico_psicologo", "TJ - Assistente Técnico – Psicólogo(a)"),
                            ("gerencia_administracao", "Gerência/Administração"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
