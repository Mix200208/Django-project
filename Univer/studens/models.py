from django.db import models

# Create your models here.
class Education(models.Model):
    ''' Основная информация'''


    adress = models.CharField("Адрес Института", max_length=60)
    name_education = models.CharField("название Института", max_length=60)
    facultet = models.CharField("Факультет", max_length=60)

    def __str__(self):
        return self.name_education
    '''Мета- это контейнер класса ,который с некоторыми опциями ,прикрепленными к модели'''
    class Meta:
        verbose_name = "Образование"
class Teacher(models.Model):
    name = models.CharField('имя преподавателя', max_length=80)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    history = models.PositiveSmallIntegerField("Стаж", default=0)
    def __str__(self):
        return self.name
    '''Мета- это контейнер класса ,который с некоторыми опциями ,прикрепленными к модели'''
    class Meta:
        verbose_name = "Учитель"



class Lesson(models.Model):
    "Основная модель нашего проекта"
    name_lesson = models.CharField('название предмета', max_length=35)

    adress = models.ForeignKey(Education, verbose_name="Образование", on_delete=models.SET_NULL, null=True)
    teacher = models.ManyToManyField(Teacher,verbose_name="Учитель")
    number_lesson = models.IntegerField("Номер аудитории", default=0)
    def __str__(self):
        return self.name_lesson
    '''Мета- это контейнер класса ,который с некоторыми опциями ,прикрепленными к модели'''
    class Meta:
        verbose_name = "Урок"


class Rate(models.Model):

    rate = models.PositiveSmallIntegerField('Оценка за предмет',default=0)
    lesson = models.ForeignKey(Lesson,verbose_name="Урок", on_delete=models.CASCADE)




    def __str__(self):
        return f"{self.lesson} - {self.rate}"
    class Meta:
        verbose_name = "Оценка"

class attendance(models.Model):
    number_visits = models.IntegerField(default=0)
    lesson = models.ForeignKey(Lesson,verbose_name="Урок", on_delete=models.CASCADE)

    def __str__(self):
        return self.number_visits
    class Meta:
        verbose_name = "Посещаемость"











