from django.urls import path
from quotes.api.views import QuoteListCreateAPIView,QuoteDetailAPIView

app_name = 'quotes'
urlpatterns = [
    path('',QuoteListCreateAPIView.as_view(),name='list'),
    path('<int:pk>/',QuoteDetailAPIView.as_view(),name='detail'),

]