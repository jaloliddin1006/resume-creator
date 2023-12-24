from rest_framework import serializers
from .models import Resume, Contact, Language


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['type', 'value']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['lang', 'level']

class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ['id', 'user', 'full_name', 'profession', 'summary', 'profile_pic', 'birthday']


