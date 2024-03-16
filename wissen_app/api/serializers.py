from rest_framework import serializers
from wissen_app.models import User, Project

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    domain = serializers.CharField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.domain = validated_data.get('domain', instance.domain)
        instance.save()
        return instance
    
class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"