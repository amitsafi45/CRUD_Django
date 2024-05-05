from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Movie
from rest_framework.decorators import action
from .serializers import MovieSerializers
from django.utils.decorators import method_decorator
from .middleware import CustomMiddleware


   

class Movies(APIView):
    @method_decorator(CustomMiddleware)
    def get(self,request:Request,format=None):
        print("Start")
        movies = Movie.objects.all()
        serializer = MovieSerializers(movies, many=True)
        return Response({"status": "success", "data":serializer.data}, status=status.HTTP_200_OK)
    
    
    def post(self,request:Request):
        req=request.data
        Movie.objects.create(name=req.get('name'), director=req.get('director'))
        return Response({"status": "success", "data": "serializer.data",}, status=status.HTTP_200_OK)


        
    def delete(self,request:Request,pk, format=None):
        return Response({"status": "success", "data": "serializer.data"}, status=status.HTTP_200_OK)

    def put(self,request:Request,pk, format=None):
        return Response({"status": "success", "data": "serializer.data","f":pk}, status=status.HTTP_200_OK)

   