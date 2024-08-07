from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    employee = models.ForeignKey(User, related_name='goals', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class GoalRating(models.Model):
    RATING_CHOICES = [(i,str(i)) for i in range(1,6)]

    goal = models.ForeignKey(Goal, related_name='ratings', on_delete=models.CASCADE)
    rater = models.ForeignKey(User, related_name='goal_ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Rating for {self.goal.title} by {self.rater.username}"
    

class FunctionalArea(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class FunctionalAreaRating(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    employee = models.ForeignKey(User, related_name='functional_area_ratings', on_delete=models.CASCADE)
    functional_area = models.ForeignKey(FunctionalArea, related_name='ratings', on_delete=models.CASCADE)
    rater = models.ForeignKey(User, related_name='functional_area_raters', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating for {self.functional_area.name} by {self.rater.username}"