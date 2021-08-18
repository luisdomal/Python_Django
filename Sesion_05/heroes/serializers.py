"""Heroes app serializers"""

from rest_framework import serializers

from .models import Hero


class HeroModelSerializer(serializers.ModelSerializer):
    """Hero model serializer"""

    class Meta:
        model = Hero
        fields = '__all__'


class HeroSerializer(serializers.Serializer):
    """Hero serializer"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    publisher = serializers.CharField(max_length=2)
    alter_ego = serializers.CharField(max_length=255)
    first_appearance = serializers.CharField(max_length=255)

    def validate_publisher(self, publisher):
        """Checks if publisher is valid"""
        if publisher not in [Hero.MARVEL, Hero.DC_COMICS]:
            raise serializers.ValidationError("Publisher choice not valid")
        return publisher

    def create(self, validated_data):
        """Creates a new hero"""
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Updates a hero"""
        instance.name = validated_data.get("name")
        instance.publisher = validated_data.get("publisher")
        instance.alter_ego = validated_data.get("alter_ego")
        instance.first_appearance = validated_data.get("first_appearance")
        instance.save()
        return instance