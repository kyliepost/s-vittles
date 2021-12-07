"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from vittlesapi.models import Family


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
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """

        gamer = Gamer.objects.get(user=request.auth.user)

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        game = Game.objects.get(pk=request.data["gameId"])


        try:
            event = Event.objects.create(
                name=request.data["name"],
                bio=request.data["bio"],
                user=user
            )
            serializer = FamilySerializer(event, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = ('id', 'name', 'bio', 'user')
