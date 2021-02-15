from rest_framework import serializers

class UserProfilSerializer(serializers.Serializer):

    email = serializers.EmailField(
        max_length=254)
    first_name = serializers.CharField(
        max_length=50)
    last_name = serializers.CharField(
        max_length=50)
    address = serializers.CharField(
        max_length=50)
    city = latitude = serializers.CharField(
        max_length=50)   
    latitude = serializers.CharField(
        max_length=50)
    longitude = serializers.CharField(
        max_length=50)
    is_staff = serializers.BooleanField(
        default=False)
