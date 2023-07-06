from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "email"]


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())]
                                   )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class DistanceMatrixSerializer(serializers.Serializer):
    origin = serializers.CharField()
    destination = serializers.CharField(required=False, allow_null=True)
    latitude = serializers.FloatField(required=False, allow_null=True)
    longitude = serializers.FloatField(required=False, allow_null=True)
    city = serializers.CharField(required=False, allow_null=True, default='Lahore')
    place_id = serializers.CharField(required=False, allow_null=True)

    def validate(self, attrs):

        if not attrs.get('destination') and not attrs.get('latitude') and not attrs.get('place_id'):
            raise ValueError('Either destination or lat long is required!')
        if attrs.get('latitude') and attrs.get('longitude'):
            attrs['lat_long'] = f'{attrs["latitude"]},{attrs["longitude"]}'

        return attrs
