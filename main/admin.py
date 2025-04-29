from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Slider, Achievement, Subscription, FAQ, About, Value, Journey, CourseLevel,
    Course, Curriculum, CurriculumSubject, Benefit, NewsItem, NewsImage, Gallery,
    Teacher, TeachingMethodology, Timetable, Message, Admission, AdmissionStep,
    ApplicationForm, Info
)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'image_preview', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['number_of_students', 'number_of_teachers', 'number_0f_partners', 'years_of_experience', 'created_at']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['sub_type_uz', 'monthly_price', 'yearly_price', 'created_at']
    search_fields = ['sub_type_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['sub_type_uz', '-created_at']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_uz', 'created_at']
    search_fields = ['question_uz', 'answer_uz']
    readonly_fields = ['created_at']
    ordering = ['question_uz', '-created_at']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ['year', 'title_uz', 'created_at']
    search_fields = ['title_uz', 'description_uz', 'year']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(CourseLevel)
class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'created_at']
    search_fields = ['title_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'level', 'duration', 'size', 'image_preview', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    list_filter = ['level']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'get_school_type_uz', 'is_active', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    list_filter = ['is_active', 'school_type_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def get_school_type_uz(self, obj):
        return obj.get_school_type_uz_display()
    get_school_type_uz.short_description = "Maktab Turi (UZ)"


@admin.register(CurriculumSubject)
class CurriculumSubjectAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'curriculum', 'created_at']
    search_fields = ['title_uz', 'curriculum__title_uz']
    list_filter = ['curriculum']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'benefits_uz', 'created_at']
    search_fields = ['title_uz', 'description_uz', 'benefits_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'image_preview', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ['news', 'image_preview']
    search_fields = ['news__title_uz']
    ordering = ['-news__created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'get_type_uz', 'image_preview', 'created_at']
    search_fields = ['title_uz']
    list_filter = ['type_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def get_type_uz(self, obj):
        return obj.get_type_uz_display()
    get_type_uz.short_description = "Turi (UZ)"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name_uz', 'last_name_uz', 'subject_uz', 'image_preview', 'phone_number']
    search_fields = ['first_name_uz', 'last_name_uz', 'subject_uz']
    readonly_fields = ['created_at']
    ordering = ['last_name_uz', 'first_name_uz']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


@admin.register(TeachingMethodology)
class TeachingMethodologyAdmin(admin.ModelAdmin):
    list_display = ['title_uz']
    search_fields = ['title_uz', 'description_uz']
    ordering = ['title_uz']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['grade', 'day', 'lesson_number', 'subject_uz']
    list_filter = ['grade', 'day', 'lesson_number']
    search_fields = ['subject_uz']
    fields = [
        'grade',
        'day',
        'lesson_number',
        ('subject_uz', 'subject_ru', 'subject_en', 'subject_de')
    ]
    readonly_fields = ['created_at']
    ordering = ['grade', 'day', 'lesson_number']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'is_read', 'is_active', 'created_at']
    list_filter = ['is_read', 'is_active']
    search_fields = ['full_name', 'email', 'msg']
    readonly_fields = ['created_at']
    ordering = ['-is_read', '-created_at']


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['dates_uz', 'exam_date_uz', 'created_at']
    search_fields = ['dates_uz', 'exam_date_uz', 'requirements_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(AdmissionStep)
class AdmissionStepAdmin(admin.ModelAdmin):
    list_display = ['order', 'title_uz', 'is_finished', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    list_filter = ['is_finished']
    readonly_fields = ['created_at']
    ordering = ['order', '-created_at']


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'grade', 'phone_number', 'is_read', 'created_at']
    search_fields = ['full_name', 'phone_number', 'description']
    list_filter = ['grade', 'is_read']
    readonly_fields = ['created_at']
    ordering = ['-is_read', '-created_at']


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['address_uz', 'long', 'lat', 'created_at']
    search_fields = ['address_uz', 'address_ru', 'address_en', 'address_de']
    fields = [
        ('long', 'lat'),
        ('address_uz', 'address_ru', 'address_en', 'address_de'),
        ('telegram_url', 'insta_url', 'facebook_url', 'linkedIn_url', 'x_url')
    ]
    readonly_fields = ['created_at']
    ordering = ['created_at']