from rest_framework import serializers

class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    sur_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    is_published = serializers.BooleanField()

    author = AuthorSerializer()
    tags = TagSerializer(many=True)