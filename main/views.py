from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Slider, Achievement, Subscription, FAQ, About, Value, Journey, CourseLevel,
    Course, Curriculum, CurriculumSubject, Benefit, NewsItem, NewsImage, Gallery, Teacher,
    TeachingMethodology, Timetable, Message, Admission, AdmissionStep, ApplicationForm, Info
)
from .serializers import (
    SliderSerializer, AchievementSerializer, SubscriptionSerializer, FAQSerializer,
    AboutSerializer, ValueSerializer, JourneySerializer, CourseLevelSerializer,
    CourseSerializer, CurriculumSerializer, CurriculumSubjectSerializer, BenefitSerializer,
    NewsItemSerializer, GallerySerializer, TeacherSerializer, TeachingMethodologySerializer,
    TimetableSerializer, MessageSerializer, AdmissionSerializer, AdmissionStepSerializer,
    ApplicationFormSerializer, InfoSerializer
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


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ValueListView(generics.ListAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class JourneyListView(generics.ListAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer


class CourseLevelListView(generics.ListAPIView):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CurriculumListView(generics.ListAPIView):
    queryset = Curriculum.objects.filter(is_active=True)
    serializer_class = CurriculumSerializer


class CurriculumSubjectListView(generics.ListAPIView):
    queryset = CurriculumSubject.objects.all()
    serializer_class = CurriculumSubjectSerializer


class BenefitListView(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class NewsItemListView(generics.ListAPIView):
    queryset = NewsItem.objects.filter(is_active=True)
    serializer_class = NewsItemSerializer


class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeachingMethodologyListView(generics.ListAPIView):
    queryset = TeachingMethodology.objects.all()
    serializer_class = TeachingMethodologySerializer


class TimetableView(APIView):
    def get(self, request):
        grade = request.query_params.get('grade')
        language = request.query_params.get('lang', 'uz')

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
            day_label = DAY_TRANSLATIONS[item['day']][language]
            weekly_timetable[day_label].append(item)
        
        return Response(weekly_timetable)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AdmissionListView(generics.ListAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AdmissionStepListView(generics.ListAPIView):
    queryset = AdmissionStep.objects.all()
    serializer_class = AdmissionStepSerializer


class ApplicationFormCreateView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer


class InfoListView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer