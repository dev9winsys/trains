from django.urls import path
from . import views
from .views import IndexView,linename_autocomplete

app_name = 'trains'
urlpatterns = [
        path('',views.IndexView.as_view(),name='index'),
        path('linename_autocomplete/',views.linename_autocomplete,name = 'linename_autocomplete'),
]
