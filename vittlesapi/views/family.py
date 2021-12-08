from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from vittlesapi.models import Family, family


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


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = ('id', 'name', 'bio', 'user')
