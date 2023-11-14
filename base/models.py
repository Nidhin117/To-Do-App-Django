from django.db import models
from django.contrib.auth.models import User

#For user info there is a default model in Django
#which can be imported and used inside other models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length=200,null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True) #Automatically updates value for new inserts

    def __str__(self):
        return self.title
    
    class Meta:
        #This controls ordering of the result set
        ordering = ['complete']
