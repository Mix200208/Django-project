from django.urls import path
from . import views
urlpatterns = [
    path('', views.LessonViews.as_view(), name = "home"),
    path('<int:pk>/',views.LessonDetailViews.as_view(),name = "detail"),
    path('rate/<int:pk>/',views.NewRateAdd.as_view(),name = "add"),
    path('rate/add/<int:pk>/',views.AddRate.as_view(), name = "rateAdd")
]
"Указываем класс ,название класса , as_view()"