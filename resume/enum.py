from enum import Enum

class LanguageLevel(Enum):
    BASIC = 'BASIC'
    INTERMEDIATE = 'INTERMEDIATE'
    ADVANCED = 'ADVANCED'
    NATIVE = 'NATIVE'
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class ContactTypes(Enum):
    PHONE = 'PHONE'
    EMAIL = 'EMAIL'
    LINKEDIN = 'LINKEDIN'
    GITHUB = 'GITHUB'
    TWITTER = 'TWITTER'
    FACEBOOK = 'FACEBOOK'
    INSTAGRAM = 'INSTAGRAM'
    WEBSITE = 'WEBSITE'
    OTHER = 'OTHER'
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)