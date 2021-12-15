from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from vittlesapi.models import familyBook


class FamilyBookView(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            family = familyBook.objects.get(pk=pk)
            serializer = FamilyBookSerializer(family, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        families = familyBook.objects.all()

        serializer = FamilyBookSerializer(
            families, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(methods=['GET'], detail=False) 
    def getCurrentUser(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields = ('id',)
    

class FamilyBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = familyBook
        fields = ('id', 'recipe', 'family', 'user')
