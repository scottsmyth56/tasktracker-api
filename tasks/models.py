from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20,choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=20,choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')])
    owner = models.ForeignKey(User, related_name="tasks",blank=True)
    shared_users = models.ManyToManyField(User, related_name="shared_tasks",blank=True)
    attachments = models.ManyToManyField('Attachment', blank=True)
    
    def __str__(self):
        return self.title
    
    
class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.file.name
    
    
    