from rest_framework import serializers
from .models import Member, Events, Rank

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['rank']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event']

class MemberSerializer(serializers.ModelSerializer):
    rank = RankSerializer(read_only=True)
    event = EventSerializer(read_only=True)
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'rank', 'event']