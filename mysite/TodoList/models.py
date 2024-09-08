from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=16)
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.task}'