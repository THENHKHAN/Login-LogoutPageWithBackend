
from django.urls import path
from . import views  # here . means ALL app (importing views from our calc app )

urlpatterns = [ # here we specify the mapping
# 1st arg keept either empty string or /   and 3rd  arg is optional.
path ( '' , views.home ,name='home'), # 1st arg= U can put / or keep empty it will represent the home page that's a standard Notation. Here home is the functions name that we need to write in the views.py file of this calc folder.
path('add', views.add , name='add')
]