from django.forms import ModelForm
from resume.models import Resume, Education, Experience, Project, Language, Interest, Contact, Skill


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ('full_name', 'profession', 'summary', 'profile_pic', 'birthday')
        

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ( 'type', 'value')
        
class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ('lang', 'level')