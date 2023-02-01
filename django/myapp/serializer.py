from rest_framework import serializers, generics, status
from .models import Member, Rank

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['rank']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'firstname', 'lastname', 'phone', 'email' , 'rank']
     