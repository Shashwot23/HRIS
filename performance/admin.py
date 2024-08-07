from django.contrib import admin
from .models import Goal, GoalRating, FunctionalArea, FunctionalAreaRating


# Register your models here.
admin.site.register(Goal)
admin.site.register(GoalRating)
admin.site.register(FunctionalArea)
admin.site.register(FunctionalAreaRating)
