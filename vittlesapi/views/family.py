from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from vittlesapi.models import Family, family
from rest_framework.decorators import action


class FamilyView(ViewSet):
    

    def retrieve(self, request, pk=None):

        try:
            family = Family.objects.get(pk=pk)
            serializer = FamilySerializer(family, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        families = Family.objects.all()

        serializer = FamilySerializer(
            families, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    def create(self, request):
        
        try:               
            family = Family.objects.create(
                user = request.auth.user,
                name = request.data["name"],
                bio = request.data['bio']
            )
            family_serializer = FamilySerializer(family, context={'request': request})
            return Response(family_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, pk=None):

        try:
            family = Family.objects.get(pk=pk)
            family.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Family.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(methods=['GET'], detail=False) 
    def getCurrentUser(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
        
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields = ('id',)   

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = ('id', 'name', 'bio', 'user')
