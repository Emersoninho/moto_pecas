from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOROR = 'TVM', 'Trocar valvula do motor'
    TROCAR_OLEO = 'TO', 'Troca de óleo'
    TROCAR_OLEO_BENGALA = 'TOB', 'Trocar óleo da bengala'
    TROCAR_BATERIA = 'TB', 'Trocar bateria'
    TROCAR_FILTROS = 'TF', 'Trocar filtros'
    TROCAR_PNEU = 'TP', 'Trocar pneu'
    TROCAR_SELA = 'TS', 'Trocar sela'