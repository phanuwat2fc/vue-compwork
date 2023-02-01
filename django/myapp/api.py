from rest_framework import serializers, viewsets, routers
from django.http import JsonResponse
from .models import Member
from .serializer import MemberSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class MemberApiView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @csrf_exempt
    def MemberApi(request):
        if request.method == 'GET':
            member = Member.objects.all()
            member_serializer = MemberSerializer(member, many = True)
            return JsonResponse(member_serializer.data, safe = False)
        
        elif request.method == 'POST':
            return JsonResponse(" Add Member ", safe = False)
           

router = routers.DefaultRouter()
router.register(r'member', MemberApiView)