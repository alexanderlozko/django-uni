from rest_framework import serializers

class BackCallSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    phone = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=100, default=None)
    datetime = serializers.DateField()