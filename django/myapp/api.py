from rest_framework import serializers, viewsets, routers
from django.http import JsonResponse
from .models import Member
from .serializer import MemberSerializer



class MemberApiView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


    

router = routers.DefaultRouter()
router.register('member', MemberApiView)