from django.urls import path
from .views import main_show 
app_name = 'Main'
urlpatterns = [
 # post views
 path('', main_show, name='main'),
 #path('<int:year>/<int:month>/<int:day>/<slug:post>/',
 #post_detail,
 #name='post_detail'),
]