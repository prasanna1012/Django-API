from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import User
from .models import Recipe
from .serializers import UserSerializer
from .serializers import RecipeSerializer


@api_view(['GET', 'POST'])
def UserList(request):

    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def RecipeList(request):

    if request.method == 'GET':
        snippets = Recipe.objects.all()
        serializer = RecipeSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['GET', 'PUT', 'DELETE'])
def RecipeDetail(request, pk):

    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecipeSerializer(recipe, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        recipe.delete()
        return HttpResponse(status=204)

  
@api_view(['GET'])
def UserRecipe(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RecipeSerializer(user.recipe)
        return JsonResponse(serializer.data)

