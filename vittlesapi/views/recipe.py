from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from vittlesapi.models import Recipe, Tag, family, recipe, familyBook


class RecipeView(ViewSet):
    
    
    def retrieve(self, request, pk=None):

        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)



    def list(self, request):

        recipes = Recipe.objects.all()
        
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            recipes = recipes.filter(tag__id=tag)

        serializer = RecipeSerializer(
            recipes, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    def create(self, request):
        
        
        try:               
            recipe = Recipe.objects.create(
                user = User.objects.get(pk=request.auth.user.id),
                name = request.data["name"],
                ingredients = request.data["ingredients"],
                description = request.data["description"]
            )
            recipe.tags.set(request.data['tags'])
            familyBook.objects.create(
                family_id = request.data['family'],
                recipe = recipe
            )
            recipe_serializer = RecipeSerializer(recipe, context={'request': request})
            return Response(recipe_serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):

        try:
            recipe = Recipe.objects.get(pk=pk)
            recipe.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def update(self, request,pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            
            recipe.user=request.auth.user
            recipe.name = request.data["name"]
            recipe.ingredients = request.data['ingredients']
            recipe.description = request.data['description']
            
            recipe.tags.set(request.data['tags'])
            recipe.familyBook_id = request.data['books']
            recipe = recipe

            
            recipe.save()
            return Response({"Message", "Recipe Updated"}, status=status.HTTP_204_NO_CONTENT)
        except Recipe.DoesNotExist as ex:
            return Response({"Message", ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({"Message", ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(methods=['GET'], detail=False) 
    def getCurrentUser(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= User
        fields = ('id', )   

class RecipeTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id','description')

class RecipeSerializer(serializers.ModelSerializer):
    
    tags = RecipeTagSerializer(many=True)
    user = UserSerializer(many=False)
    
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'description', 'tags', 'books', 'user')
        depth = 3


