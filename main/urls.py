from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    SliderListView, AchievementListView, SubscriptionListView,
    FAQListView, CourseListView, NewsItemListView,
    GalleryListView, TeacherListView, TimetableView,
    MessageCreateView, AdmissionListView, LocationListView
)

urlpatterns = [
    path('sliders/', SliderListView.as_view(), name='slider-list'),
    path('achievements/', AchievementListView.as_view(), name='achievement-list'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('news/', NewsItemListView.as_view(), name='news-list'),
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('timetable/', TimetableView.as_view(), name='timetable'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('admissions/', AdmissionListView.as_view(), name='admission-list'),
    path('locations/', LocationListView.as_view(), name='locations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)