from rest_framework import serializers, viewsets, routers
from .models import Member
from .serializer import MemberSerializer

class MemberApiView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

router = routers.DefaultRouter()
router.register(r'member/list', MemberApiView)