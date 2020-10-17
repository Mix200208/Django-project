from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Lesson, Rate
from .forms import RateLesson
from .services import change_rate


# Create your views here.


class LessonViews(ListView):
    # Список уроков"
    model = Lesson
    lessons = Lesson.objects.all()

class LessonDetailViews(DetailView):
     # описания урока'
     model = Lesson
     # указываем поле,по которому нужно искать запись

     slug_field = "id"

     '''Нет необходимости писать имя шаблона,потому что джанго по имени модели подставляет _detail(суфикс) и находит
     необходимый шаблон.Работает,когда имя шаблона подходит под суффикс наследуемого класса.ListView - (_list)'''


class NewRateAdd(DetailView):
    model = Rate
    # указываем поле,по которому нужно искать запись
    slug_field = "lesson_id"
    context_object_name = "rate"
    template_name = "studens/add_rate.html"



"Добавление Оценки"
class AddRate(View):

    def post(self,request,pk):
        print(request.POST)
        form = RateLesson(request.POST)
        rate = Rate.objects.get(id=pk)

        # Значение из формы"
        if form.is_valid():
            form = form.save(commit=False)
            change_rate(request.POST.get("rate"),rate,form)


        return redirect("/")




