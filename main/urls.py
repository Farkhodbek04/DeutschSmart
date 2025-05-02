
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    SliderListView, AchievementListView, SubscriptionListView, AdmissionDiscountListView, FAQListView,
    AboutListView, ValueListView, JourneyListView, CourseLevelListView,
    CourseListView, CurriculumListView, CurriculumSubjectListView, BenefitListView,
    NewsItemListView, GalleryListView, TeacherListView, TeachingMethodologyListView,
    TimetableView, MessageCreateView, AdmissionListView, AdmissionStepListView,
    ApplicationFormCreateView, InfoListView
)

urlpatterns = [
    path('sliders/', SliderListView.as_view(), name='slider-list'),
    path('achievements/', AchievementListView.as_view(), name='achievement-list'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
    path('admission-discount/', AdmissionDiscountListView.as_view(), name='admission-discount-list'),
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('about/', AboutListView.as_view(), name='about-list'),
    path('values/', ValueListView.as_view(), name='value-list'),
    path('journeys/', JourneyListView.as_view(), name='journey-list'),
    path('course-levels/', CourseLevelListView.as_view(), name='course-level-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('curriculums/', CurriculumListView.as_view(), name='curriculum-list'),
    path('curriculum-subjects/', CurriculumSubjectListView.as_view(), name='curriculum-subject-list'),
    path('benefits/', BenefitListView.as_view(), name='benefit-list'),
    path('news/', NewsItemListView.as_view(), name='news-item-list'),   
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teaching-methodologies/', TeachingMethodologyListView.as_view(), name='teaching-methodology-list'),
    path('timetable/', TimetableView.as_view(), name='timetable'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('admissions/', AdmissionListView.as_view(), name='admission-list'),
    path('admission-steps/', AdmissionStepListView.as_view(), name='admission-step-list'),
    path('application-forms/', ApplicationFormCreateView.as_view(), name='application-form-create'),
    path('info/', InfoListView.as_view(), name='info-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)