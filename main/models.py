from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class Slider(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    image = models.ImageField(upload_to='school/sliders/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Slayder"
        verbose_name_plural = "Slayderlar"
        ordering = ['-created_at']


class Achievement(models.Model):
    number_of_students = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])
    number_of_teachers = models.PositiveIntegerField(validators=[MaxValueValidator(1000)])
    number_0f_partners = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    years_of_experience = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Yutuqlar (Yangilangan: {self.created_at})"

    class Meta:
        verbose_name = "Yutuq"
        verbose_name_plural = "Yutuqlar"
        ordering = ['-created_at']


class Subscription(models.Model):
    SUB_TYPE_CHOICES_UZ = [
        ('Asosiy', 'Asosiy'),
        ('Standart', 'Standart'),
        ('Premium', 'Premium'),
    ]
    SUB_TYPE_CHOICES_RU = [
        ('Базовый', 'Базовый'),
        ('Стандартный', 'Стандартный'),
        ('Премиум', 'Премиум'),
    ]
    SUB_TYPE_CHOICES_EN = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]
    SUB_TYPE_CHOICES_DE = [
        ('Basis', 'Basis'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    sub_type_uz = models.CharField(max_length=20, choices=SUB_TYPE_CHOICES_UZ, blank=True)
    sub_type_ru = models.CharField(max_length=20, choices=SUB_TYPE_CHOICES_RU, blank=True)
    sub_type_en = models.CharField(max_length=20, choices=SUB_TYPE_CHOICES_EN, blank=True)
    sub_type_de = models.CharField(max_length=20, choices=SUB_TYPE_CHOICES_DE, blank=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    yearly_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def get_sub_type(self, language='en'):
        """Get the sub_type in the specified language."""
        return getattr(self, f'sub_type_{language}', self.sub_type_en)

    def __str__(self):
        """Return a string representation using the English sub_type (or another default)."""
        return f"{self.get_sub_type('en')} Obuna"

    class Meta:
        verbose_name = "Obuna"
        verbose_name_plural = "Obunalar"
        ordering = ['sub_type_uz', '-created_at']


class FAQ(models.Model):
    question_uz = models.CharField(max_length=255)
    question_ru = models.CharField(max_length=255)
    question_en = models.CharField(max_length=255)
    question_de = models.CharField(max_length=255)
    answer_uz = models.TextField()
    answer_ru = models.TextField()
    answer_en = models.TextField()
    answer_de = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.question_uz

    class Meta:
        verbose_name = "Savol-Javob"
        verbose_name_plural = "Savol-Javoblar"
        ordering = ['question_uz', '-created_at']


class About(models.Model): ####
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name_plural = "Biz haqimizda"
        ordering = ['-created_at']
        
        
class Value(models.Model): ###
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name_plural = "Bizning qiymatimiz"
        ordering = ['-created_at']
        

class Journey(models.Model): ####
    year = models.CharField(max_length=5)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name_plural = "Bizning sayohat"
        ordering = ['-created_at']
    

class CourseLevel(models.Model): ###
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title_uz
    
    class Meta:
        verbose_name_plural = "Kurs darajalari"
        ordering = ['-created_at']
    
    


class Course(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    image = models.ImageField(upload_to='school/courses/')
    duration = models.CharField(max_length=100)
    level = models.ForeignKey(CourseLevel, on_delete=models.SET_NULL, null=True)
    size = models.PositiveSmallIntegerField()
    highlights = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-created_at']


class Curriculum(models.Model): ###
    
    SCHOOL_TYPE_CHOICES_UZ = [
    (0, 'Boshlang\'ich'),
    (1, 'O\'rta'),
    (2, 'Yuqori'),
    ]

    SCHOOL_TYPE_CHOICES_RU = [
        (0, 'Начальная'),
        (1, 'Средняя'),
        (2, 'Старшая'),
    ]

    SCHOOL_TYPE_CHOICES_EN = [
        (0, 'Elementary'),
        (1, 'Middle'),
        (2, 'High'),
    ]

    SCHOOL_TYPE_CHOICES_DE = [
        (0, 'Grundschule'),
        (1, 'Mittelschule'),
        (2, 'Oberschule'),
    ]
    school_type_uz = models.IntegerField(choices=SCHOOL_TYPE_CHOICES_UZ, blank=True, null=True)
    school_type_ru = models.IntegerField(choices=SCHOOL_TYPE_CHOICES_RU, blank=True, null=True)
    school_type_en = models.IntegerField(choices=SCHOOL_TYPE_CHOICES_EN, blank=True, null=True)
    school_type_de = models.IntegerField(choices=SCHOOL_TYPE_CHOICES_DE, blank=True, null=True)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "O'quv dasturi "
        verbose_name_plural = "O'quv dasturlari"
        ordering = ['-created_at']
    
class CurriculumSubject(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return f"{self.title_uz} fani - {self.curriculum.title_uz}"

    class Meta:
        verbose_name_plural = "O'quv dasturi fanlari"  
        ordering = ['-created_at']
    
    
class Benefit(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    benefits_uz = models.CharField(max_length=200)
    benefits_ru = models.CharField(max_length=200)
    benefits_en = models.CharField(max_length=200)
    benefits_de = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name_plural = "Bizning ta'limni foydalari"
        ordering = ['-created_at']


class NewsItem(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    image = models.ImageField(upload_to='school/news/')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']


class NewsImage(models.Model):
    image = models.ImageField(upload_to='school/news/')
    news = models.ForeignKey('NewsItem', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.news.title_uz} uchun rasm"

    class Meta:
        verbose_name = "Yangilik Rasmi"
        verbose_name_plural = "Yangilik Rasmlari"
        ordering = ['-news__created_at']


class Gallery(models.Model):
    TYPE_CHOICES_UZ = [
    (0, 'Hammasi'),
    (1, 'Maktab Hayoti'),
    (2, 'Akademik'),
    (3, 'Sanat va Musiqa'),
    (4, 'Tadbirlar'),
    ]

    TYPE_CHOICES_RU = [
        (0, 'Все'),
        (1, 'Школьная жизнь'),
        (2, 'Академический'),
        (3, 'Искусство и музыка'),
        (4, 'Мероприятия'),
    ]

    TYPE_CHOICES_EN = [
        (0, 'All'),
        (1, 'School Life'),
        (2, 'Academic'),
        (3, 'Art & Music'),
        (4, 'Events'),
    ]

    TYPE_CHOICES_DE = [
        (0, 'Alle'),
        (1, 'Schulleben'),
        (2, 'Akademisch'),
        (3, 'Kunst & Musik'),
        (4, 'Veranstaltungen'),
    ]

    type_uz = models.IntegerField(choices=TYPE_CHOICES_UZ, blank=True, null=True)
    type_ru = models.IntegerField(choices=TYPE_CHOICES_RU, blank=True, null=True)
    type_en = models.IntegerField(choices=TYPE_CHOICES_EN, blank=True, null=True)
    type_de = models.IntegerField(choices=TYPE_CHOICES_DE, blank=True, null=True)
    image = models.ImageField(upload_to='school/gallery/')
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    title_de = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Galereya Rasmi {self.type_uz}"

    class Meta:
        verbose_name_plural = "Galereya"
        ordering = ['-created_at']


class Teacher(models.Model):
    first_name_uz = models.CharField(max_length=100)
    first_name_ru = models.CharField(max_length=100)
    first_name_en = models.CharField(max_length=100)
    first_name_de = models.CharField(max_length=100)
    last_name_uz = models.CharField(max_length=100)
    last_name_ru = models.CharField(max_length=100)
    last_name_en = models.CharField(max_length=100)
    last_name_de = models.CharField(max_length=100)
    image = models.ImageField(upload_to='school/teachers/')
    subject_uz = models.CharField(max_length=255)
    subject_ru = models.CharField(max_length=255)
    subject_en = models.CharField(max_length=255)
    subject_de = models.CharField(max_length=255)
    edu_level_uz = models.CharField(max_length=100)
    edu_level_ru = models.CharField(max_length=100)
    edu_level_en = models.CharField(max_length=100)
    edu_level_de = models.CharField(max_length=100)
    num_of_experience = models.PositiveSmallIntegerField()
    languages = models.CharField(max_length=255)
    bio_uz = models.TextField(blank=True)
    bio_ru = models.TextField(blank=True)
    bio_en = models.TextField(blank=True)
    bio_de = models.TextField(blank=True)
    certifications_uz = models.TextField(blank=True)
    certifications_ru = models.TextField(blank=True)
    certifications_en = models.TextField(blank=True)
    certifications_de = models.TextField(blank=True)
    from_country = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=14,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Noto'g'ri telefon raqami")]
    )
    telegram_url = models.URLField(verbose_name='Telegram havola')
    insta_url = models.URLField(verbose_name='Instagram havola', null=True, blank=True)
    facebook_url = models.URLField(verbose_name='Facebook havola', null=True, blank=True)
    linkedIn_url = models.URLField(verbose_name='LinkedIN havola', null=True, blank=True)
    x_url = models.URLField(verbose_name='X havola', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.first_name_uz} {self.last_name_uz} - {self.subject_uz}"

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
        ordering = ['last_name_uz', 'first_name_uz']
        
        
class TeachingMethodology(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    
    def __str__(self):
            return self.title_uz

    class Meta:
        verbose_name_plural = "O'qitish metodologiyalari"
        ordering = ['title_uz'  ]

class Timetable(models.Model):
    class Grade(models.IntegerChoices):
        GRADE_1 = 1, "1"
        GRADE_2 = 2, "2"
        GRADE_3 = 3, "3"
        GRADE_4 = 4, "4"
        GRADE_5 = 5, "5"
        GRADE_6 = 6, "6"
        GRADE_7 = 7, "7"
        GRADE_8 = 8, "8"
        GRADE_9 = 9, "9"
        GRADE_10 = 10, "10"
        GRADE_11 = 11, "11"

    class Day(models.TextChoices):
        MONDAY = "Dushanba", "Dushanba"
        TUESDAY = "Seshanba", "Seshanba"
        WEDNESDAY = "Chorshanba", "Chorshanba"
        THURSDAY = "Payshanba", "Payshanba"
        FRIDAY = "Juma", "Juma"
        SATURDAY = "Shanba", "Shanba"

    class Lesson(models.IntegerChoices):
        LESSON_1 = 1, "1"
        LESSON_2 = 2, "2"
        LESSON_3 = 3, "3"
        LESSON_4 = 4, "4"
        LESSON_5 = 5, "5"
        LESSON_6 = 6, "6"
        LESSON_7 = 7, "7"
        
    grade = models.IntegerField(choices=Grade.choices, help_text="Sinflar (1-11)")
    day = models.CharField(max_length=12, choices=Day.choices, help_text="Hafta kunlari")
    lesson_number = models.IntegerField(choices=Lesson.choices, help_text="Darslar tartibi")
    subject_uz = models.CharField(max_length=50, help_text="Dars fani (O'zbekcha)")
    subject_ru = models.CharField(max_length=50, help_text="Dars fani (Ruscha)")
    subject_en = models.CharField(max_length=50, help_text="Dars fani (Inglizcha)")
    subject_de = models.CharField(max_length=50, help_text="Dars fani (Nemischacha)")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.grade}-sinf - {self.day} - {self.subject_uz} {self.lesson_number}-dars"

    class Meta:
        verbose_name_plural = "Dars Jadvali"
        ordering = ['grade', 'day', 'lesson_number']
        unique_together = ['grade', 'day', 'lesson_number']

class Message(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Murojat"
        verbose_name_plural = "Murojatlar"
        ordering = ['-is_read', '-created_at']
    
    
class Admission(models.Model):
    dates_uz = models.TextField()
    dates_ru = models.TextField()
    dates_en = models.TextField()
    dates_de = models.TextField()
    exam_date_uz = models.TextField()
    exam_date_ru = models.TextField()
    exam_date_en = models.TextField()
    exam_date_de = models.TextField()
    requirements_uz = models.TextField()
    requirements_ru = models.TextField()
    requirements_en = models.TextField()
    requirements_de = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def get_field(self, field_name, language='uz'):
        return getattr(self, f'{field_name}_{language}', getattr(self, f'{field_name}_uz', ''))

    def __str__(self):
        return self.get_field('dates', 'uz')

    class Meta:
        verbose_name_plural = "Qabul jarayoni"
        ordering = ['-created_at']
        

class AdmissionStep(models.Model): ###
    order = models.PositiveSmallIntegerField()
    is_finished = models.BooleanField(verbose_name='Jarayonda')
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255)
    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    description_de = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name_plural = "Qabul bosqichlari"
        ordering = ['-created_at']
        
        
class ApplicationForm(models.Model):
    class Grade(models.IntegerChoices):
        GRADE_1 = 1, "1"
        GRADE_2 = 2, "2"
        GRADE_3 = 3, "3"
        GRADE_4 = 4, "4"
        GRADE_5 = 5, "5"
        GRADE_6 = 6, "6"
        GRADE_7 = 7, "7"
        GRADE_8 = 8, "8"
        GRADE_9 = 9, "9"
        GRADE_10 = 10, "10"
        GRADE_11 = 11, "11"
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(
        max_length=14,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Noto'g'ri telefon raqami")]
    )
    grade = models.IntegerField(choices=Grade.choices, help_text="Sinflar (1-11)")
    description = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.grade}-sinf"
    
    class Meta:
        verbose_name_plural = "Qabul so'rovlari"
        ordering = ['-is_read', '-created_at']
    
    
class Info(models.Model):
    long = models.FloatField(help_text="Kenglik (Longitude)")
    lat = models.FloatField(help_text="Uzunlik (Latitude)")
    address_uz = models.CharField(max_length=255, help_text="Manzil (O'zbekcha)")
    address_ru = models.CharField(max_length=255, help_text="Manzil (Ruscha)")
    address_en = models.CharField(max_length=255, help_text="Manzil (Inglizcha)")
    address_de = models.CharField(max_length=255, help_text="Manzil (Nemischacha)")
    phone_number = models.CharField(
        max_length=14,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Noto'g'ri telefon raqami")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    telegram_url = models.URLField(verbose_name='Telegram havola')
    insta_url = models.URLField(verbose_name='Instagram havola')
    facebook_url = models.URLField(verbose_name='Facebook havola')
    linkedIn_url = models.URLField(verbose_name='LinkedIN havola')
    x_url = models.URLField(verbose_name='X havola')

    def __str__(self):
        return self.address_uz

    class Meta:
        verbose_name_plural = "Maktab info"
        ordering = ['created_at']