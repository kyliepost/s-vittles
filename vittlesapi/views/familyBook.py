from django.contrib.auth.models import User
from django.http import HttpResponseServerError
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
    

class FamilyBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = familyBook
        fields = ('id', 'recipe', 'family')
        depth = 1