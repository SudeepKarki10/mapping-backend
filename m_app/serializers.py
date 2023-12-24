from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['business_name', 'email', 'phone_number', 'address','password',]



    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

        

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['location'] = {
        'latitude': instance.latitude,
        'longitude': instance.longitude
    }
        return representation
