from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Slider, Achievement, Subscription, FAQ, Course, NewsItem,
    Gallery, Teacher, Timetable, Message, Admission, Location
)
from .serializers import (
    SliderSerializer, AchievementSerializer, SubscriptionSerializer,
    FAQSerializer, CourseSerializer, NewsItemSerializer,
    GallerySerializer, TeacherSerializer, TimetableSerializer,
    MessageSerializer, AdmissionSerializer, LocationSerializer
)

# Static day translations for response keys
DAY_TRANSLATIONS = {
    "Dushanba": {'uz': 'Dushanba', 'ru': 'Понедельник', 'en': 'Monday', 'de': 'Montag'},
    "Seshanba": {'uz': 'Seshanba', 'ru': 'Вторник', 'en': 'Tuesday', 'de': 'Dienstag'},
    "Chorshanba": {'uz': 'Chorshanba', 'ru': 'Среда', 'en': 'Wednesday', 'de': 'Mittwoch'},
    "Payshanba": {'uz': 'Payshanba', 'ru': 'Четверг', 'en': 'Thursday', 'de': 'Donnerstag'},
    "Juma": {'uz': 'Juma', 'ru': 'Пятница', 'en': 'Friday', 'de': 'Freitag'},
    "Shanba": {'uz': 'Shanba', 'ru': 'Суббота', 'en': 'Saturday', 'de': 'Samstag'},
}


class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class AchievementListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class SubscriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NewsItemListView(generics.ListAPIView):
    queryset = NewsItem.objects.filter(is_active=True)
    serializer_class = NewsItemSerializer


class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TimetableView(APIView):
    def get(self, request):
        grade = request.query_params.get('grade')
        language = request.query_params.get('lang', 'uz')
        print(f"Received language: {language}")

        if not grade:
            return Response({"error": "Grade parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            grade = int(grade)
            if grade not in [choice[0] for choice in Timetable.Grade.choices]:
                return Response({"error": "Invalid grade (must be 1-11)"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "Grade must be a number"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate language
        valid_languages = ['uz', 'ru', 'en', 'de']
        if language not in valid_languages:
            language = 'uz'

        # Fetch timetable for the specified grade
        timetable = Timetable.objects.filter(grade=grade).order_by('day', 'lesson_number')
        
        # Structure the response by day
        days = [DAY_TRANSLATIONS[day[0]][language] for day in Timetable.Day.choices]
        weekly_timetable = {day: [] for day in days}
        
        # Serialize all items with context
        serializer = TimetableSerializer(timetable, many=True, context={'request': request})
        for item in serializer.data:
            day_label = item['day']
            weekly_timetable[day_label].append(item)
        
        return Response(weekly_timetable)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AdmissionListView(generics.ListAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    
    
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    