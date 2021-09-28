
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from cloudsek_app.models import Amount

class AmountSerializer(serializers.ModelSerializer):
    id_pk= serializers.CharField(max_length=300)
    number_1 = serializers.IntegerField()
    number_2 = serializers.IntegerField()
    total = serializers.IntegerField()


    class Meta:
        model = Amount
        fields = '__all__'


class AmountResultSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()


    class Meta:
        model = Amount
        fields = ["total"]