
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import manage_item

urlpatterns = {
    path('search', manage_item, name="single_item")
}

urlpatterns = format_suffix_patterns(urlpatterns)