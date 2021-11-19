from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import valueModel,csvmodel
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token


class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = valueModel
        fields = "__all__"

class csvserializer(serializers.ModelSerializer):
    class Meta:
        model = csvmodel
        fields = "__all__"