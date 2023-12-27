from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from resume.enum import LanguageLevel, ContactTypes

class BaseModels(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
        
class ResumeTemplates(BaseModels):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='templates/', null=True,  blank=True, default='templates/default.png')
    
    def __str__(self):
        return self.name
    

class Resume(BaseModels):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    template = models.ForeignKey('ResumeTemplates', on_delete=models.CASCADE, related_name='resumes', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    summary = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True,  blank=True, default='profile_pics/default.png')
    birthday = models.DateField(default='2000-12-31')
    
    class Meta:
        ordering = ['-created_at',]
    def __str__(self):
        return self.full_name
    

    
class Contact(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='contacts')
    type = models.CharField(max_length=50, choices=ContactTypes.choices(), verbose_name='Type', default=ContactTypes.EMAIL)
    value = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type
    

class Skill(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Education(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='educations')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    currently = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Experience(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return self.company
    

class Project(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    year = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Language(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='languages')
    lang = models.CharField(max_length=50, verbose_name='Language')
    level = models.CharField(max_length=50, choices=LanguageLevel.choices(), verbose_name='Level')
    
    def __str__(self):
        return self.lang
    
    
class Interest(BaseModels):
    resume = models.ForeignKey('Resume', on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    