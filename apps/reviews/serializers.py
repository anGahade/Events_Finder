from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'event', 'user', 'rating', 'comment', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(ReviewSerializer, self).create(validated_data)
