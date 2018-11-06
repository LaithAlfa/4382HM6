from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='Index'),
    path('Index.html', HomePageView.as_view(), name='Index'),
    path('About.html/Index.html', HomePageView.as_view(), name='Index'),
	path('About.html/', AboutPageView.as_view(), name='About'),
]