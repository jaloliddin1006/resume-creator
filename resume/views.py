from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django import views
from resume.models import Resume, Contact, Skill, Education, Experience, Project, Language, Interest
from resume.forms import ResumeForm, ContactForm, LanguageForm
from rest_framework import response
from rest_framework import generics
from rest_framework.views import APIView
from resume.serializers import ResumeSerializer

from django.shortcuts import redirect

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
        # print(request.POST)
      
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
            context = {
                "resume" : resume,
                # "contact" : contact,
                # "language" : language,
            }
            # return render(request, "tmpl/resume1.html", context)
            return redirect(reverse('resume:resume-view', kwargs={'pk': resume.id}))
   
        context = {
            'resume': resume,
            'contact': contact,
            'language': language,
        }
        return render(request, "resume/information.html", context)
        # return response.Response({"message": "Success"}, status=200)
        
    
    
class ResumeRetrieveAPIView(generics.RetrieveAPIView):
    # print("ResumeRetrieveView")
    
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    lookup_field = 'pk'
    # print("ResumeRetrieveView", queryset)
    
class ResumeRetriveView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)  
        resume = Resume.objects.get(id=kwargs['pk'])
        contact = Contact.objects.get(resume=resume)
        language = Language.objects.get(resume=resume)
        education = Education.objects.filter(resume=resume)
        exprience = Experience.objects.filter(resume=resume)
        project = Project.objects.filter(resume=resume)
        skill = Skill.objects.filter(resume=resume)
        interest = Interest.objects.filter(resume=resume)
        
        context = {
            'resume': resume,
            'contact': contact,
            'language': language,
            'education': education,
            'exprience': exprience,
            'project': project,
            'skill': skill,
            'interest': interest,
        }
        
        
        return render(request, "tmpl/resume1.html", context)
          
    
