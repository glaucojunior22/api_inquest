from rest_framework import serializers
from core.models import Person, Enterprise, Possession

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class PossessionSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(
        max_digits=10, decimal_places=2, localize=True
    )
    nome_propietario = serializers.SerializerMethodField()


    def get_nome_proprietario(self, obj):
        return obj.owner.name
    
    class Meta:
        model = Possession
        fields = '__all__'