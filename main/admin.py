from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Slider, Achievement, Subscription, FAQ, Course,
    NewsItem, NewsImage, Gallery, Teacher, Timetable, Message, Admission, Location
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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'image_preview', 'created_at']
    search_fields = ['title_uz', 'description_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"


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


# @admin.register(NewsImage)
# class NewsImageAdmin(admin.ModelAdmin):
#     list_display = ['news', 'image_preview']
#     search_fields = ['news__title_uz']
#     ordering = ['-news__created_at']

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
#         return "Rasm yo'q"
#     image_preview.short_description = "Rasm"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'created_at']
    readonly_fields = ['created_at']
    ordering = ['-created_at']

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
    list_display = ['dates_uz', 'created_at']
    search_fields = ['dates_uz', 'requirements_uz', 'steps_uz']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['address_uz', 'long', 'lat', 'created_at']
    search_fields = ['address_uz', 'address_ru', 'address_en', 'address_de']
    fields = [
        ('long', 'lat'),
        ('address_uz', 'address_ru', 'address_en', 'address_de')
    ]
    readonly_fields = ['created_at']
    ordering = ['created_at']