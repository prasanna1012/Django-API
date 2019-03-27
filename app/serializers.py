from rest_framework import serializers
from .models import User
from .models import Recipe
from .models import Ingredient
from .models import Step


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'lastname')
    #   fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = '__all__'


