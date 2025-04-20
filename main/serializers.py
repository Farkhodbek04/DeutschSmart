from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Slider, Achievement, Subscription, FAQ, Course, NewsItem,
    NewsImage, Gallery, Teacher, Timetable, Message, Admission, Location
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
    sub_type_uz = serializers.CharField(source='get_sub_type', read_only=True)

    class Meta:
        model = Subscription
        exclude = ['id', 'created_at']


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ['id', 'created_at']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id', 'created_at']


class NewsImageSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        exclude = ['id']


class NewsItemSerializer(ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = NewsItem
        exclude = ['id', 'created_at', 'is_active']


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ['id', 'created_at']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ['id', 'created_at']


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
        exclude = ['id', 'created_at',]


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
        
        
class AdmissionSerializer(ModelSerializer):
    class Meta:
        model = Admission
        exclude = ['id', 'created_at']


class LocationSerializer(ModelSerializer):
    address = serializers.SerializerMethodField()

    def get_address(self, obj):
        language = self.get_language()
        return getattr(obj, f'address_{language}')

    def get_language(self):
        language = self.context.get('request').query_params.get('language', 'uz') if self.context.get('request') else 'uz'
        valid_languages = ['uz', 'ru', 'en', 'de']
        return language if language in valid_languages else 'uz'

    class Meta:
        model = Location
        exclude = ['id', 'created_at']