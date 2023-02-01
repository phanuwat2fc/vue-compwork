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
    rank_name = serializers.CharField(source="rank")
    class Meta:
        model = Member
        fields = ['email','id','firstname','lastname','rank_name','event','phone']