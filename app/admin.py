from django.contrib import admin

from .models import User
from .models import Recipe
from .models import Ingredient
from .models import Step


admin.site.register(User)

admin.site.register(Recipe)

admin.site.register(Ingredient)

admin.site.register(Step)