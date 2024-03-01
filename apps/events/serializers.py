from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)
    free_tickets = serializers.IntegerField(read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'organizer', 'rating', 'category', 'title', 'description', 'image', 'num_of_seats', 'date',
                  'venue', 'free_tickets']

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        validated_data['free_tickets'] = validated_data['num_of_seats']
        return super(EventSerializer, self).create(validated_data)
