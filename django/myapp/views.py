from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Member
from .serializer import MemberSerializer



# Create your views here.
@csrf_exempt
def MemberApi(request):
    if request.method == 'GET':
        member = Member.objects.all()
        member_serializer = MemberSerializer(member, many = True)
        return JsonResponse(member_serializer.data, safe = False)
    
    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(data = member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse("Add Member Success" , safe = False)
        return JsonResponse("Failed Add Member", safe = False)
        
def MemberDetail(request, pk):

    members = Member.objects.get(pk=pk)
    print(members)
    return JsonResponse("member " + str(pk), safe = False)
    if request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass