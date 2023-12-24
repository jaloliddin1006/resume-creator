from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from resume.models import Resume, Contact, Skill, Education, Experience, Project, Language, Interest
from resume.forms import ResumeForm, ContactForm, LanguageForm
from rest_framework import response
from rest_framework import generics
from rest_framework.views import APIView
from resume.serializers import ResumeSerializer

    

class ResumeInformationView(View):
    def get(self, request, *args, **kwargs):
        resume = ResumeForm(prefix="resume")
        contact = ContactForm(prefix="contact")
        language = LanguageForm(prefix="language")
        
        context = {
            'resume': resume,
            'contact': contact,
            'language': language,
        }
        return render(request, "resume/information.html", context)
    def post(self, request, *args, **kwargs):
        user = request.user
      
        resume = ResumeForm(request.POST, request.FILES, prefix="resume")
        contact = ContactForm(request.POST, prefix="contact")
        language = LanguageForm(request.POST, prefix="language")

        if resume.is_valid() and contact.is_valid() and language.is_valid():
            
            resume = resume.save(commit=False)
            contact = contact.save(commit=False)
            language = language.save(commit=False)
            
            resume.user = user
            
            resume.save()
            contact.resume = resume
            contact.save()
            language.resume = resume
            language.save()
            print("success", resume.id)
            return render(request, "index.html", {})
   
        context = {
            'resume': resume,
            'contact': contact,
            'language': language,
        }
        return render(request, "resume/information.html", context)
        # return response.Response({"message": "Success"}, status=200)
        
        