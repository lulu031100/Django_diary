#自分で作った アプリケーション用のurl
from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'), # http://127.0.0.1:8000/diary/
    path('add/',views.AddView.as_view(), name='add'), # http://127.0.0.1:8000/diary/add/
]