from django.urls import path
# from .api_views import WordList
from . import generic_views

urlpatterns = [
    # path('words/', WordList.as_view(), name="word")
    path('words/', generic_views.ListCreateWord.as_view(), name='word_list'),
    path('words/<int:pk>', generic_views.RetrieveUpdateDestroyWord.as_view(), name='word_detail'),
]