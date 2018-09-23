from django.conf.urls import url
from django.urls import path

from squirrel import settings
from squirrel.settings import MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company-list'),
    path('details/<int:pk>/', views.CompanyDetailsView.as_view(), name='company-details'),
    path('review/', views.ReviewCreateView.as_view(), name='review-create'),
    path('get_pdf/', views.SendPDF.as_view(), name='GetPDF')
]

