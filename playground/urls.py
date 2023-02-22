from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns =[
    path('hello/', views.say_hello),
    path('_debug_/', include(debug_toolbar.urls))
]