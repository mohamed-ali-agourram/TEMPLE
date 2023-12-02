from django.urls import path
from .views import (
    TempleDetailView,
    TempelListView,
    search,
    AboutUs,
    ContactUs
)

urlpatterns = [
    path('', TempelListView.as_view(), name="templates"),
    path('search/', search, name="search"),
    path("aboutus/", AboutUs, name="aboutus"),
    path('contactus/', ContactUs, name="contactus"),
    path('template/<int:pk>/', TempleDetailView.as_view(), name="template-detail")
]
