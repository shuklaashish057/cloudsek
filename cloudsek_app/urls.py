from django.urls import path
from .views import AmountView, ResultView
from cloudsek_app import views

urlpatterns = [

    path('',AmountView.as_view()),
    path('calculate/number1/number2',AmountView.as_view()),
    path('getanswer/<str:uuid>', ResultView.as_view())

]