from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='start_page'),
    path('candidate/', CandCreate.as_view(), name='candidate'),
    path('candidate/questions/', Question_answer.as_view(), name='questins'),
    path('jedi/', JediView.as_view(), name='jedis'),
    path('jedi/<int:id>/', Jedi_name, name='jedi_name'),
    path('jedi/<int:id>/cand<int:id_cand>', Jedi_cand, name='jedi_cand')
]