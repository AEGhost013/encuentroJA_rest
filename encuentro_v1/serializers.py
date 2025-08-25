from rest_framework import serializers
from models import *

#serializador de perfiles
class PerfilSerializer(serializers.ModelSerializer):
    class meta:
        model = Perfil
        fields = ['user_perfil', 'edad', 'bam_usuario', 'evento', 'puntaje']
        
class BamSerializer(serializers.ModelSerializer):
    class meta:
        model = Bam
        fields = ['nombre_bam', 'lider']
        
class EventoSerializer(serializers.ModelSerializer):
    class meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion_evento']