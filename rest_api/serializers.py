from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from base.models import ReservaModel, Petshop


class PetshopNestedSerializer(serializers.ModelSerializer):
    reservas = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:reservamodel-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Petshop
        fields = '__all__'


class ReservaModelSerializer(serializers.ModelSerializer):
    petshop = PetshopNestedSerializer(read_only=True)

    class Meta:
        model = ReservaModel
        fields = '__all__'

