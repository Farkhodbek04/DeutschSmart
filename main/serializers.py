from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Slider, Achievement, Subscription, AdmissionDiscount, FAQ, About, Value, Journey, CourseLevel,
    Course, Curriculum, CurriculumSubject, Benefit, NewsItem, NewsImage, Gallery,
    Teacher, TeachingMethodology, Timetable, Message, Admission, AdmissionStep,
    ApplicationForm, Info
)

# Static day translations
DAY_TRANSLATIONS = {
    "Dushanba": {'uz': 'Dushanba', 'ru': 'Понедельник', 'en': 'Monday', 'de': 'Montag'},
    "Seshanba": {'uz': 'Seshanba', 'ru': 'Вторник', 'en': 'Tuesday', 'de': 'Dienstag'},
    "Chorshanba": {'uz': 'Chorshanba', 'ru': 'Среда', 'en': 'Wednesday', 'de': 'Mittwoch'},
    "Payshanba": {'uz': 'Payshanba', 'ru': 'Четверг', 'en': 'Thursday', 'de': 'Donnerstag'},
    "Juma": {'uz': 'Juma', 'ru': 'Пятница', 'en': 'Friday', 'de': 'Freitag'},
    "Shanba": {'uz': 'Shanba', 'ru': 'Суббота', 'en': 'Saturday', 'de': 'Samstag'},
}

class SliderSerializer(ModelSerializer):
    class Meta:
        model = Slider
        exclude = ['id', 'created_at']

class AchievementSerializer(ModelSerializer):
    class Meta:
        model = Achievement
        exclude = ['id', 'created_at']

class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        exclude = ['id', 'created_at']
        
        
class AdmissionDiscountSerializer(ModelSerializer):

    class Meta:
        model = AdmissionDiscount
        exclude = ['id', 'created_at']

class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ['id', 'created_at']

class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        exclude = ['id', 'created_at']

class ValueSerializer(ModelSerializer):
    class Meta:
        model = Value
        exclude = ['id', 'created_at']

class JourneySerializer(ModelSerializer):
    class Meta:
        model = Journey
        exclude = ['id', 'created_at']

class CourseLevelSerializer(ModelSerializer):
    class Meta:
        model = CourseLevel
        exclude = ['id', 'created_at']

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id', 'created_at']

class CurriculumSerializer(ModelSerializer):
    school_type = serializers.SerializerMethodField()

    def get_school_type(self, obj):
        language = self.get_language()
        return getattr(obj, f'get_school_type_{language}_display')()

    def get_language(self):
        language = self.context.get('request').query_params.get('language', 'uz') if self.context.get('request') else 'uz'
        valid_languages = ['uz', 'ru', 'en', 'de']
        return language if language in valid_languages else 'uz'

    class Meta:
        model = Curriculum
        exclude = ['id', 'created_at', 'is_active']

class CurriculumSubjectSerializer(ModelSerializer):
    class Meta:
        model = CurriculumSubject
        exclude = ['id', 'created_at']

class BenefitSerializer(ModelSerializer):
    class Meta:
        model = Benefit
        exclude = ['id', 'created_at']

class NewsImageSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['image']  # Exclude 'news' and 'id' for cleaner output

class NewsItemSerializer(ModelSerializer):
    image = serializers.ImageField()  # Serialize the NewsItem's image field as a URL
    images = NewsImageSerializer(many=True, read_only=True, source='newsimage_set')  # Use the reverse relation

    class Meta:
        model = NewsItem
        exclude = ['id', 'is_active']

class GallerySerializer(ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        language = self.get_language()
        return getattr(obj, f'get_type_{language}_display')()

    def get_language(self):
        language = self.context.get('request').query_params.get('language', 'uz') if self.context.get('request') else 'uz'
        valid_languages = ['uz', 'ru', 'en', 'de']
        return language if language in valid_languages else 'uz'

    class Meta:
        model = Gallery
        exclude = ['id', 'created_at']

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ['id', 'created_at']

class TeachingMethodologySerializer(ModelSerializer):
    class Meta:
        model = TeachingMethodology
        exclude = ['id']

class TimetableSerializer(ModelSerializer):
    day = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()

    def get_day(self, obj):
        language = self.get_language()
        return DAY_TRANSLATIONS.get(obj.day, {}).get(language, obj.day)

    def get_subject(self, obj):
        language = self.get_language()
        return getattr(obj, f'subject_{language}')

    def get_language(self):
        language = self.context.get('request').query_params.get('language', 'uz') if self.context.get('request') else 'uz'
        valid_languages = ['uz', 'ru', 'en', 'de']
        return language if language in valid_languages else 'uz'

    class Meta:
        model = Timetable
        exclude = ['id', 'created_at']

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        exclude = ['id', 'is_active', 'is_read', 'created_at']
        extra_kwargs = {
            'is_active': {'read_only': True},
            'is_read': {'read_only': True},
            'created_at': {'read_only': True}
        }

class AdmissionSerializer(ModelSerializer):
    class Meta:
        model = Admission
        exclude = ['id', 'created_at']

class AdmissionStepSerializer(ModelSerializer):
    class Meta:
        model = AdmissionStep
        exclude = ['id', 'created_at', 'is_finished']

class ApplicationFormSerializer(ModelSerializer):
    class Meta:
        model = ApplicationForm
        exclude = ['id', 'is_read', 'created_at']
        extra_kwargs = {
            'is_read': {'read_only': True},
            'created_at': {'read_only': True}
        }

class InfoSerializer(ModelSerializer):
    address = serializers.SerializerMethodField()

    def get_address(self, obj):
        language = self.get_language()
        return getattr(obj, f'address_{language}')

    def get_language(self):
        language = self.context.get('request').query_params.get('language', 'uz') if self.context.get('request') else 'uz'
        valid_languages = ['uz', 'ru', 'en', 'de']
        return language if language in valid_languages else 'uz'

    class Meta:
        model = Info
        exclude = ['id', 'created_at']