import re
from django.shortcuts import render
from .serializer import DrugSerializer
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from .models import Drug

# Create your views here.
@api_view(['GET'])
def Overview(request):
    apis=[
        {
            "drug-add/":"drug-add",
            "drug-list/":"drug-list",
            "drug-update/<int:pk>/":"drug-update",
            "drug-delete/<int:pk>/":"drug-delete",
        }
    ]

    return Response(apis);

@api_view(['GET'])
def DrugList(request):
    drugs=Drug.objects.all()
    serializer=DrugSerializer(drugs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AddGrug(request):
    drug=DrugSerializer(data=request.data)
    if drug.is_valid():
        drug.save()

    return Response("Drug added successfully !")

@api_view(['POST'])
def UpadateDrug(request,pk):
    drug=Drug.objects.get(id=pk)
    serializer=DrugSerializer(instance=drug,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Updated successfully !")

@api_view(['DELETE'])
def Delete(request , pk):
    drug=Drug.objects.get(id=pk)
    drug.delete()
    return Response("Deleted successfully !")
