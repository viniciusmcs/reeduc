"""Create Agendamento model."""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration for Agendamento."""

    dependencies = [
        ("core", "0003_atendimento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agendamento",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome_atendido", models.CharField(max_length=255)),
                (
                    "tipo_agendamento",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("acompanhamento", "Acompanhamento"),
                            ("atendimento", "Atendimento"),
                            ("cadastro", "Cadastro"),
                            ("retorno", "Retorno"),
                            ("outro", "Outro"),
                        ],
                        max_length=20,
                    ),
                ),
                ("data_agendamento", models.DateField()),
                (
                    "horario_atendimento",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("07:00", "7:00"),
                            ("07:30", "7:30"),
                            ("08:00", "8:00"),
                            ("08:30", "8:30"),
                            ("09:00", "9:00"),
                            ("09:30", "9:30"),
                            ("10:00", "10:00"),
                            ("10:30", "10:30"),
                            ("11:00", "11:00"),
                            ("11:30", "11:30"),
                            ("12:00", "12:00"),
                            ("12:30", "12:30"),
                            ("13:00", "13:00"),
                            ("13:30", "13:30"),
                            ("14:00", "14:00"),
                            ("14:30", "14:30"),
                            ("15:00", "15:00"),
                            ("15:30", "15:30"),
                            ("16:00", "16:00"),
                        ],
                        max_length=5,
                    ),
                ),
                ("observacoes", models.TextField(blank=True)),
            ],
        ),
    ]
