from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=50)
    comment = serializers.CharField(max_length=50)
    datetime = serializers.DateField()
    published = serializers.BooleanField(default=False)