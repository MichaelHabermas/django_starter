from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Note(models.Model):
    note_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False, default="new note")
    body = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False)
    age = models.IntegerField(blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)