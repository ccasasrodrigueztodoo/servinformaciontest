from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class ApiProfileView(APIView):
    serializer_class = serializers.UserProfilSerializer
    def get(self, request, format=None):
        
        an_apiview = [
            'This api is created to add',
            'new users',

            
        ]
        return Response({'hello': 'Api - New users', 'an_apiview': an_apiview})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('first_name')
            message = f"Hello {name}"

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
    
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})


