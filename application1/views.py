from django.shortcuts import render
from .models import Disease
from .serializers import DiseaseSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class DiseaseViewset(viewsets.ViewSet):
    def getalldata(self,request):
        data = Disease.objects.all()
        seri = DiseaseSerializer(data,many = True)
        return Response(seri.data)
    
    def getbyid(self,request,id):
        data = Disease.objects.get(Did=id)
        seri = DiseaseSerializer(data)
        return Response(seri.data)
    def createdisease(self,request):
        print("callll..")
        seri = DiseaseSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response({'msg':'created..'})
