from django.urls import path
from .views import NovelListCreateAPIView,NovelDetailAPIView,ReviewCreateAPIView,ReviewDetailAPIView

app_name = 'ebook'
urlpatterns = [
    path('novels/',NovelListCreateAPIView.as_view(),name= 'novel'),

   
    
    path('<int:pk>/',NovelDetailAPIView.as_view(),name='detail'),
    path('review/create/<int:novel_pk>/',ReviewCreateAPIView.as_view(),name='create_reviewe'), 
    path('review/<int:pk>/',ReviewDetailAPIView.as_view(),name='detail_review'),
    

]